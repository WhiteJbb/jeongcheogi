# 정처기 실기 스터디

정보처리기사 실기 기출(복원) 풀이 + 핵심 개념 + 용어 암기카드. 빌드 도구 없이 `index.html` 하나로 동작.

## 기능
- 회차별·과목별·언어별(C/Java/Python/SQL) 기출 풀이, 자동 채점, 오답노트
- 실전 모의고사: 실제 출제 비율(코드 8·SQL 2·용어 10)로 20문항 추출, 150분 타이머, 100점 채점, 점수 이력
- 핵심 개념 12과목 + 기출 자동 연결(출제 횟수 표시), 용어 암기카드, 통합 검색

## 공부 방법
`docs/gap-analysis.md` — 출제 구조·배점 전략, 2주/4주 학습 로드맵, 자료의 한계.

## 사용
- 온라인: GitHub Pages (저장소 설정 참고)
- 로컬: `python3 build.py` 후 아무 정적 서버로 열기 (예: `python3 -m http.server`)

## 데이터 추가
`data/exams/<년>-<회>.json`, `data/concepts/<nn>-<slug>.json` 에 추가 → `python3 build.py` → `data.js` 갱신.
스키마는 `data/SCHEMA.md`.

풀이 기록·암기카드 상태는 브라우저 localStorage에만 저장됨.
