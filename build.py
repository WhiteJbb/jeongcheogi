#!/usr/bin/env python3
"""data/ 의 JSON을 data.js 하나로 묶는다. 실행: python3 build.py"""
import json, glob, os
root = os.path.dirname(os.path.abspath(__file__))
def load(pattern):
    out = []
    for f in sorted(glob.glob(os.path.join(root, pattern))):
        try:
            out.append(json.load(open(f, encoding="utf-8")))
        except Exception as e:
            raise SystemExit(f"{f}: {e}")
    return out
exams = load("data/exams/*.json")
SUBJ = {"요구사항 확인","데이터 입출력 구현","통합 구현","서버 프로그램 구현","인터페이스 구현","화면 설계",
        "애플리케이션 테스트 관리","SQL 응용","소프트웨어 개발 보안 구축","프로그래밍 언어 활용","응용 SW 기초 기술 활용","제품 소프트웨어 패키징"}
errs = []
for e in exams:
    for q in e["questions"]:
        tag = f'{e["year"]}-{e["round"]} #{q.get("no")}'
        if q.get("subject") not in SUBJ: errs.append(f"{tag}: subject '{q.get('subject')}'")
        if not q.get("answer") or not all(isinstance(a, str) and a.strip() for a in q["answer"]): errs.append(f"{tag}: answer 비어 있음")
        if not q.get("question", "").strip(): errs.append(f"{tag}: question 비어 있음")
        if q.get("type") == "코드" and not q.get("code"): errs.append(f"{tag}: 코드 문제인데 code 없음 (경고)")
    nos = [q.get("no") for q in e["questions"]]
    if len(nos) != len(set(nos)): errs.append(f'{e["year"]}-{e["round"]}: no 중복')
if errs: print("\n".join(errs))
concepts = sorted(load("data/concepts/*.json"), key=lambda c: c.get("order", 99))
# 개념 토픽 ↔ 기출 자동 연결: 문항 keywords/answer 가 토픽 제목·용어와 정확히 일치하면 asked 에 회차 추가
import re
nk = lambda t: re.sub(r"[\s\-_/·.,()]", "", t).lower()
def names(t):
    out = {nk(t["title"])}
    for term in t.get("terms", []):
        for part in re.split(r"\s*[()]\s*", term["term"]):
            if len(nk(part)) >= 2: out.add(nk(part))
    return out
linked = 0
for c in concepts:
    for t in c["topics"]:
        ns = names(t); asked = set(t.get("asked", []))
        for e in exams:
            rid = f'{e["year"]}-{e["round"]}'
            for q in e["questions"]:
                cands = [nk(k) for k in q.get("keywords", [])] + [nk(a) for a in q.get("answer", []) if q.get("type") != "코드"]
                if any(x in ns for x in cands if len(x) >= 2):
                    if rid not in asked: linked += 1
                    asked.add(rid)
        t["asked"] = sorted(asked, key=lambda r: tuple(map(int, r.split("-"))))
print(f"auto-linked {linked} topic↔round pairs")
data = {"exams": exams, "concepts": concepts}
with open(os.path.join(root, "data.js"), "w", encoding="utf-8") as fp:
    fp.write("window.DATA=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n")
nq = sum(len(e["questions"]) for e in exams)
nt = sum(len(c["topics"]) for c in concepts)
print(f"exams={len(exams)} questions={nq} chapters={len(concepts)} topics={nt}")
