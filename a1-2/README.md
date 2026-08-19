# 국내 여행 추천 프로그램 (LLM + 지도 API)

여행 날짜를 입력하면 **LLM API**가 해당 시기에 여행하기 좋은 국내 지역을 추천하고,
**지도/장소 검색 API**로 그 지역의 맛집을 찾은 뒤, 다시 LLM이 **최종 여행 리포트(Markdown)**를
생성하는 CLI 프로그램입니다.

```
CLI(--date) ─▶ [1/3] LLM 1차 추천(JSON) ─▶ [2/3] 지도 API 맛집 검색 ─▶ [3/3] LLM 리포트(MD)
```

## 프로그램 개요

| 단계 | 내용 | HTTP |
|------|------|------|
| 1차 추천 | LLM이 `recommended_city / weather / events / reason`을 **JSON**으로 생성 | POST |
| 맛집 검색 | 추천 도시로 맛집 최대 5곳 검색 (`name/address/category/url/x/y`) | GET |
| 리포트 생성 | 1차 추천 + 맛집 목록을 입력받아 **Markdown 리포트** 생성 | POST |

- **LLM 제공자**: OpenAI 또는 Google Gemini (`--llm` 로 선택)
- **지도 제공자**: Kakao Local 또는 Naver Local Search (`--map` 으로 선택)
- 실제 키가 없어도 `--mock` 으로 전체 흐름을 검증할 수 있습니다.

## 요구 환경

- Python **3.10 이상**
- 의존성: `requests`, `python-dotenv` (`requirements.txt`)

## 설치

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## API 키 설정 방법

키는 **코드에 직접 작성하지 않고** 환경변수 또는 `.env` 파일에서 읽어옵니다.

### 방법 1) `.env` 파일 (권장)

```bash
cp .env.example .env
# .env 를 열어 사용할 제공자의 키 값만 채웁니다.
```

`.env` 예시 (택1씩):

```
# LLM (택1)
OPENAI_API_KEY=sk-...
# 또는
GEMINI_API_KEY=...

# 지도 (택1)
KAKAO_REST_API_KEY=...
# 또는
NAVER_CLIENT_ID=...
NAVER_CLIENT_SECRET=...
```

### 방법 2) 환경변수 (현재 터미널 세션에만 적용)

```bash
# macOS / Linux
export OPENAI_API_KEY="YOUR_KEY"
export KAKAO_REST_API_KEY="YOUR_KEY"
```
```powershell
# Windows PowerShell
$env:OPENAI_API_KEY="YOUR_KEY"
$env:KAKAO_REST_API_KEY="YOUR_KEY"
```

| 환경변수 | 용도 |
|----------|------|
| `OPENAI_API_KEY` | OpenAI 사용 시 (`OPENAI_MODEL` 선택, 기본 `gpt-4o-mini`) |
| `GEMINI_API_KEY` | Gemini 사용 시 (`GEMINI_MODEL` 선택, 기본 `gemini-1.5-flash`) |
| `KAKAO_REST_API_KEY` | Kakao Local 사용 시 |
| `NAVER_CLIENT_ID` / `NAVER_CLIENT_SECRET` | Naver Local 사용 시 |

## 실행 방법

```bash
# 기본 (OpenAI + Kakao)
python travel_planner.py --date 2026-03-15

# 제공자 지정
python travel_planner.py --date 2026-03-15 --llm gemini --map naver

# 복수 지역 추천(보너스) — 2곳
python travel_planner.py --date 2026-03-15 --multi 2

# 캐싱(보너스) — 같은 날짜 원본 JSON이 있으면 API 호출을 건너뛰고 리포트만 재생성
python travel_planner.py --date 2026-03-15 --cache

# 키 없이 전체 흐름 테스트
python travel_planner.py --date 2026-03-15 --mock
```

### 옵션

| 옵션 | 기본값 | 설명 |
|------|--------|------|
| `-d`, `--date` | (필수) | 여행 날짜 `YYYY-MM-DD`. 형식이 틀리면 사용법을 출력하고 종료 |
| `--llm` | `openai` | LLM 제공자: `openai` \| `gemini` |
| `--map` | `kakao` | 지도 제공자: `kakao` \| `naver` |
| `--multi` | `1` | 추천 지역 개수 (보너스) |
| `--count` | `5` | 도시별 맛집 검색 개수 |
| `--mock` | off | 실제 API 없이 샘플 데이터로 실행 |
| `--cache` | off | 원본 JSON 재사용 (보너스) |

### 실행 예시 출력

```
[1/3] 1차 추천 생성 중(LLM)...
    - recommended_city: 제주
[2/3] 맛집 검색 중(지도/장소 API)...
    - [제주] 맛집 5곳 검색 완료
[3/3] 최종 리포트 생성 중(LLM)...
    - 리포트 생성 완료

완료! results/2026-03-15_travel_plan.md 를 확인하세요.
      원본 데이터: results/2026-03-15_raw.json
```

## 결과물 확인 방법

실행하면 `results/` 폴더에 날짜 기준으로 두 파일이 생성됩니다.

| 파일 | 내용 |
|------|------|
| `results/{date}_raw.json` | 원본 데이터: 1차 추천 JSON + 맛집 검색 결과 + `errors` 배열 |
| `results/{date}_travel_plan.md` | 최종 여행 리포트 (Markdown) |

리포트 섹션: `추천 지역 / 추천 이유 / 날씨 요약 / 행사·축제 / 맛집 추천 / 1일 일정 제안 / 오류 요약(errors)`

## 에러 처리 정책

| 상황 | 동작 |
|------|------|
| LLM API 키 미설정 | 즉시 종료 + 설정 방법 안내 |
| 지도 API 실패(인증 401/403·네트워크·쿼터) | 맛집 섹션을 **"데이터 없음"** 처리하고 리포트는 계속 생성 |
| 맛집 검색 0건 | 중단하지 않고 "데이터 없음"으로 다음 단계 진행 |
| LLM JSON 파싱 실패 | **1회만** 재요청("필수 키만 JSON으로 출력") |

발생한 오류는 내부 `errors[]`로 누적되어 원본 JSON과 리포트의 "오류 요약" 섹션에 남습니다.

## ⚠️ 보안 주의 사항 (중요)

- **API 키를 코드·README·결과물(JSON/MD/로그)에 직접 작성하지 마세요.**
- 키는 반드시 `.env` 또는 환경변수로 관리합니다. `.env` 는 `.gitignore` 에 포함되어 커밋되지 않습니다.
- `.env.example` 에는 키 **이름만** 있고 값은 비어 있습니다. 실수로 값 채운 파일을 커밋하지 않도록 주의하세요.
- 왜 필요한가:
  - 협업/공유 시 실수로 키가 공개되는 것을 막습니다.
  - 키를 교체해도 코드를 수정할 필요가 없습니다(운영/배포에 유리).
  - 과금/쿼터가 걸린 서비스에서 사고를 예방합니다.

## 파일 구조

```
a1-2/
├── travel_planner.py   # 메인 CLI (argparse, 3단계 오케스트레이션)
├── llm_client.py       # LLM 호출 (1차 추천 JSON + 최종 리포트)
├── place_client.py     # 지도 API 맛집 검색 (Kakao / Naver)
├── report.py           # Markdown 리포트 생성(폴백 포함)
├── errors.py           # 표준 예외(Auth/Network/Parse/Api)
├── requirements.txt
├── .env.example        # 키 이름만 (값 없음)
├── .gitignore          # .env, results/ 제외
└── results/            # 실행 시 생성 (원본 JSON + 리포트 MD)
```
