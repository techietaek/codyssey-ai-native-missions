# 에러 상황 재현 기록 (input → output)

외부 API 호출/입력 검증에서 발생하는 대표 오류를 실제로 재현하고,
프로그램이 어떻게 반응하는지(메시지 + 종료 코드)를 기록한다.
아래 두 시나리오는 네트워크/실제 API 호출 없이 100% 재현된다.

실행 환경: `.venv/bin/python`, 작업 디렉터리 `a1-2/`

---

## 시나리오 A — 잘못된 날짜 형식 (입력 검증 실패)

**의도:** `--date`에 `YYYY-MM-DD`가 아닌 값을 넣으면, API를 호출하기도 전에
입력 검증 단계(`validate_date`)에서 걸러져야 한다.

### input
```bash
$ python travel_planner.py --date 2026/05/10
```

### output
```
[오류] 날짜 형식이 올바르지 않습니다: '2026/05/10'
       올바른 형식: --date "YYYY-MM-DD" (예: 2026-03-15)
```

### 결과
- 종료 코드(exit code): **2**
- 결과 파일 생성 안 됨 (검증 실패로 즉시 종료)
- 처리 위치: `travel_planner.py:66-74` (`validate_date` → `SystemExit(2)`)

---

## 시나리오 B — API 키 미설정 (인증 준비 실패)

**의도:** LLM API 키가 없으면, 실제 호출로 401을 맞기 전에 사전 점검
단계(`check_keys`)에서 친절한 안내와 함께 종료해야 한다.

> 재현 방법: 환경변수 `OPENAI_API_KEY`를 빈 값으로 덮어써서 "키 없음" 상태를 만든다.
> (`.env`에 실제 키가 있어도, 이미 설정된 환경변수를 `load_dotenv`가 덮어쓰지 않으므로 빈 값이 유지된다.)

### input
```bash
$ OPENAI_API_KEY= python travel_planner.py --date 2026-05-10
```

### output
```
[오류] OpenAI LLM API 키가 설정되지 않았습니다.
       .env 파일 또는 환경변수로 아래 키를 설정하세요:
         OPENAI_API_KEY
       예) export OPENAI_API_KEY="YOUR_KEY"
       (실제 키 없이 테스트하려면 --mock 옵션을 사용하세요.)
```

### 결과
- 종료 코드(exit code): **1**
- 결과 파일 생성 안 됨 (키 점검 실패로 즉시 종료)
- 처리 위치: `travel_planner.py:88-97` (`check_keys`) → `:77-85` (`die_missing_key` → `SystemExit(1)`)

---

## 정리

| 시나리오 | 원인 | 처리 단계 | 종료 코드 | 파일 생성 |
|---|---|---|---|---|
| A | 날짜 형식 오류 | `validate_date` | 2 | X |
| B | API 키 미설정 | `check_keys` / `die_missing_key` | 1 | X |

- 두 오류 모두 **API를 호출하기 전에** 미리 걸러진다(빠른 실패, fail-fast).
- 종료 코드를 서로 다르게(2 = 입력 오류, 1 = 실행 전제 조건 오류) 구분해,
  스크립트/자동화에서 원인을 구별할 수 있다.
- 실행 중(런타임) 발생하는 오류(인증 401/403, 쿼터 429, 네트워크, 파싱)는
  `errors.py`의 표준 예외로 변환되어, 단계에 따라
  중단(1차 추천) 또는 `errors[]` 기록 후 계속 진행(맛집 검색/리포트)된다.
