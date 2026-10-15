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
concepts = sorted(load("data/concepts/*.json"), key=lambda c: c.get("order", 99))
data = {"exams": exams, "concepts": concepts}
with open(os.path.join(root, "data.js"), "w", encoding="utf-8") as fp:
    fp.write("window.DATA=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n")
nq = sum(len(e["questions"]) for e in exams)
nt = sum(len(c["topics"]) for c in concepts)
print(f"exams={len(exams)} questions={nq} chapters={len(concepts)} topics={nt}")
