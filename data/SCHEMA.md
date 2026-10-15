# 데이터 스키마

## data/exams/<year>-<round>.json  (예: 2024-3.json, 2020-4.json)
```json
{
  "year": 2024, "round": 3, "date": "2024-10-19",
  "questions": [
    {
      "no": 1,
      "subject": "프로그래밍 언어 활용",
      "type": "코드",          // "코드" | "단답" | "서술" | "SQL" | "빈칸"
      "lang": "Java",          // 코드/SQL 문제만. "C" | "Java" | "Python" | "SQL"
      "question": "다음 Java 코드의 출력 결과를 쓰시오.",
      "code": "public class Main {...}",   // 코드가 있으면. 없으면 생략
      "answer": ["7"],         // 정답 표기 후보들(동의어/허용표기 모두). 채점은 공백·대소문자 무시 비교
      "explanation": "실행 순서 설명... (3~5줄 이내, 핵심만)",
      "keywords": ["재귀", "static"],
      "source": "https://..."  // 복원 출처 URL (있으면)
    }
  ]
}
```
- subject는 아래 12개 중 하나만 사용:
  요구사항 확인 / 데이터 입출력 구현 / 통합 구현 / 서버 프로그램 구현 / 인터페이스 구현 /
  화면 설계 / 애플리케이션 테스트 관리 / SQL 응용 / 소프트웨어 개발 보안 구축 /
  프로그래밍 언어 활용 / 응용 SW 기초 기술 활용 / 제품 소프트웨어 패키징
- 빈칸 문제가 여러 개(①②③)면 answer를 ["① A, ② B, ③ C"] 처럼 하나로 합치고, `blanks: ["A","B","C"]`도 함께 넣는다.
- 코드는 탭 대신 공백 4칸, 줄바꿈은 \n.

## data/concepts/<nn>-<slug>.json  (예: 01-requirements.json)
```json
{
  "chapter": "요구사항 확인", "order": 1,
  "topics": [
    {
      "title": "결합도 (Coupling)",
      "importance": 3,        // 1~3, 3=매년 나옴
      "summary": "모듈 간 상호 의존 정도. 낮을수록 좋음.",
      "points": ["자료 < 스탬프 < 제어 < 외부 < 공통 < 내용 (약→강)", "암기: 자스제외공내"],
      "terms": [{"term": "스탬프 결합도", "desc": "배열/구조체 등 자료구조를 전달"}],
      "asked": ["2020-1", "2022-2"]   // 출제 회차 (알면)
    }
  ]
}
```
