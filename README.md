# 정처기 실기 스터디

정보처리기사 실기 기출(복원) 풀이 + 핵심 개념 + 용어 암기카드. 빌드 도구 없이 `index.html` 하나로 동작.

## 사용
- 온라인: GitHub Pages (저장소 설정 참고)
- 로컬: `python3 build.py` 후 아무 정적 서버로 열기 (예: `python3 -m http.server`)

## 데이터 추가
`data/exams/<년>-<회>.json`, `data/concepts/<nn>-<slug>.json` 에 추가 → `python3 build.py` → `data.js` 갱신.
스키마는 `data/SCHEMA.md`.

풀이 기록·암기카드 상태는 브라우저 localStorage에만 저장됨.
