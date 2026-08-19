"""나만의 프롬프트 관리 - 콘솔 프로그램

파편화된 프롬프트를 카테고리별로 관리하고 검색/즐겨찾기까지 지원한다.
데이터는 리스트(list)와 딕셔너리(dict)로 관리하며, 프로그램 실행 중에만 유지된다.
"""

import json
import os

# 데이터 파일 및 내보내기 폴더 경로
DATA_FILE = "prompts_data.json"
EXPORT_DIR = "exports"

# 미리 정의된 카테고리 목록
CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

# 이전 미션에서 작성한 프롬프트를 기본 데이터로 등록 (최소 3개 이상)
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": (
            "당신은 10년 경력의 전문 블로거입니다.\n"
            "주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요.\n"
            "서론, 본론, 결론 구조를 갖추고, 독자의 관심을 끄는 제목을 3개 제안해주세요."
        ),
        "category": "텍스트 생성",
        "favorite": True,
    },
    {
        "title": "제품 썸네일 생성",
        "content": (
            "다음 제품의 매력적인 썸네일 이미지를 생성해주세요.\n"
            "밝고 깨끗한 배경, 부드러운 조명, 제품이 중앙에 배치된 구도.\n"
            "스타일: 미니멀, 고급스러움. 비율: 1:1."
        ),
        "category": "이미지 생성",
        "favorite": False,
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": (
            "당신은 15년 경력의 IT 전략 컨설턴트입니다.\n"
            "비전문가도 이해할 수 있도록 기술 개념을 쉬운 비유로 설명하고,\n"
            "항상 근거와 실행 가능한 다음 단계를 함께 제시합니다."
        ),
        "category": "페르소나",
        "favorite": False,
    },
    {
        "title": "뉴스 요약 자동화 프롬프트",
        "content": (
            "아래 뉴스 기사를 3문장으로 요약하고, 핵심 키워드 5개를 뽑아주세요.\n"
            "마지막에 한 줄로 시사점을 정리해주세요."
        ),
        "category": "자동화",
        "favorite": False,
    },
    {
        "title": "광고 스크립트 작성",
        "content": (
            "15초 분량의 짧은 광고 영상 스크립트를 작성해주세요.\n"
            "장면(Scene) 단위로 나누고, 각 장면의 화면 묘사와 나레이션을 함께 적어주세요."
        ),
        "category": "영상 생성",
        "favorite": False,
    },
]


def star(prompt):
    """즐겨찾기 여부를 별표(⭐) 문자열로 반환한다."""
    return " ⭐" if prompt["favorite"] else ""


def input_required(label):
    """값이 비어있으면 다시 입력받는 필수 입력 함수."""
    while True:
        value = input(label).strip()
        if value:
            return value
        print("값이 비어있습니다. 다시 입력해주세요.")


def choose_category():
    """카테고리를 미리 정의된 목록에서 선택하거나 직접 입력받는다."""
    print("\n카테고리 선택:")
    for i, name in enumerate(CATEGORIES, start=1):
        print(f"{i}) {name}")
    print("(목록에 없으면 직접 입력하세요.)")

    choice = input("선택: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
        return CATEGORIES[int(choice) - 1]
    # 숫자가 아니거나 범위를 벗어나면 직접 입력한 카테고리로 처리
    return choice if choice else "기타"


def add_prompt():
    """새 프롬프트를 등록한다. 즐겨찾기 기본값은 False."""
    print("\n=== 프롬프트 추가 ===")
    title = input_required("제목: ")
    content = input_required("내용: ")
    category = choose_category()

    prompts.append(
        {"title": title, "content": content, "category": category, "favorite": False}
    )
    print("\n프롬프트가 추가되었습니다!")


def print_prompt_lines(items):
    """(번호, 프롬프트) 목록을 '[카테고리] 제목 ⭐' 형식으로 출력한다."""
    for i, prompt in enumerate(items, start=1):
        print(f"{i}. [{prompt['category']}] {prompt['title']}{star(prompt)}")


def show_list():
    """저장된 모든 프롬프트를 번호와 함께 출력한다."""
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    print_prompt_lines(prompts)
    print(f"\n총 {len(prompts)}개의 프롬프트")


def show_by_category():
    """카테고리를 선택하면 해당 카테고리의 프롬프트만 출력한다."""
    print("\n=== 카테고리별 조회 ===")
    for i, name in enumerate(CATEGORIES, start=1):
        print(f"{i}) {name}")

    choice = input("선택: ").strip()
    if not (choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES)):
        print("잘못된 번호입니다.")
        return

    category = CATEGORIES[int(choice) - 1]
    found = [p for p in prompts if p["category"] == category]

    print(f"\n[{category}] 카테고리 프롬프트:")
    if not found:
        print("해당 카테고리에 프롬프트가 없습니다.")
        return

    print_prompt_lines(found)
    print(f"\n총 {len(found)}개의 프롬프트")


def search_prompt():
    """키워드로 제목 또는 내용에 포함된 프롬프트를 검색한다."""
    print("\n=== 프롬프트 검색 ===")
    keyword = input("검색어: ").strip()
    if not keyword:
        print("검색어가 비어있습니다.")
        return

    lowered = keyword.lower()
    found = [
        p for p in prompts
        if lowered in p["title"].lower() or lowered in p["content"].lower()
    ]

    print("\n검색 결과:")
    if not found:
        print("검색 결과가 없습니다.")
        return

    print_prompt_lines(found)
    print(f"\n{len(found)}개의 프롬프트를 찾았습니다.")


def read_index(label):
    """현재 프롬프트 목록을 먼저 보여준 뒤, 1부터 시작하는 번호를 입력받는다.
    유효하면 인덱스를, 아니면 None을 반환한다."""
    print("\n현재 프롬프트 목록:")
    print_prompt_lines(prompts)
    raw = input(label).strip()
    if not raw.isdigit():
        print("숫자를 입력해주세요.")
        return None
    idx = int(raw) - 1
    if not (0 <= idx < len(prompts)):
        print("잘못된 번호입니다.")
        return None
    return idx


def show_detail():
    """프롬프트 번호를 입력하면 전체 내용을 출력하고 조회수를 기록한다(보너스)."""
    print("\n=== 프롬프트 상세 보기 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    idx = read_index("번호 입력: ")
    if idx is None:
        return

    prompt = prompts[idx]
    prompt["views"] = prompt.get("views", 0) + 1  # 보너스: 조회수 기록

    line = "─" * 28
    print(line)
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {'⭐' if prompt['favorite'] else '없음'}")
    print(f"조회수: {prompt['views']}")
    print(line)
    print("내용:")
    print(prompt["content"])
    print(line)


def toggle_favorite():
    """프롬프트 번호를 입력받아 즐겨찾기를 추가/해제한다."""
    print("\n=== 즐겨찾기 관리 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    idx = read_index("프롬프트 번호 입력: ")
    if idx is None:
        return

    prompt = prompts[idx]
    prompt["favorite"] = not prompt["favorite"]
    if prompt["favorite"]:
        print(f"'{prompt['title']}' 프롬프트를 즐겨찾기에 추가했습니다!")
    else:
        print(f"'{prompt['title']}' 프롬프트를 즐겨찾기에서 해제했습니다!")


def show_favorites():
    """즐겨찾기된 프롬프트만 모아서 출력한다."""
    print("\n=== 즐겨찾기 목록 ===")
    found = [p for p in prompts if p["favorite"]]
    if not found:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return

    print_prompt_lines(found)
    print(f"\n총 {len(found)}개의 즐겨찾기")


def edit_prompt():
    """프롬프트 번호를 입력받아 제목/내용/카테고리를 수정한다(보너스). 빈 입력은 유지."""
    print("\n=== 프롬프트 수정 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    idx = read_index("수정할 번호 입력: ")
    if idx is None:
        return

    prompt = prompts[idx]
    print("(비워두고 Enter 시 기존 값 유지)")
    new_title = input(f"제목 [{prompt['title']}]: ").strip()
    new_content = input("내용 (기존 유지하려면 Enter): ").strip()

    if new_title:
        prompt["title"] = new_title
    if new_content:
        prompt["content"] = new_content

    change_cat = input("카테고리를 변경할까요? (y/N): ").strip().lower()
    if change_cat == "y":
        prompt["category"] = choose_category()

    print("프롬프트가 수정되었습니다!")


def delete_prompt():
    """프롬프트 번호를 입력받아 삭제한다(보너스)."""
    print("\n=== 프롬프트 삭제 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    idx = read_index("삭제할 번호 입력: ")
    if idx is None:
        return

    confirm = input(f"'{prompts[idx]['title']}'을(를) 삭제할까요? (y/N): ").strip().lower()
    if confirm == "y":
        removed = prompts.pop(idx)
        print(f"'{removed['title']}' 프롬프트를 삭제했습니다.")
    else:
        print("삭제를 취소했습니다.")


def show_top_viewed():
    """조회수 기준 내림차순으로 상위 프롬프트를 출력한다(보너스)."""
    print("\n=== 조회수 Top 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    ranked = sorted(prompts, key=lambda p: p.get("views", 0), reverse=True)
    for i, prompt in enumerate(ranked, start=1):
        views = prompt.get("views", 0)
        print(f"{i}. [{prompt['category']}] {prompt['title']}{star(prompt)} (조회수 {views})")


def save_to_json():
    """전체 프롬프트를 JSON 파일로 저장한다(보너스1)."""
    print("\n=== JSON 저장 ===")
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=2)
    print(f"'{DATA_FILE}' 파일에 {len(prompts)}개의 프롬프트를 저장했습니다.")


def load_from_json():
    """JSON 파일에서 프롬프트를 불러온다(보너스1). 기존 데이터는 대체된다."""
    print("\n=== JSON 불러오기 ===")
    if not os.path.exists(DATA_FILE):
        print(f"'{DATA_FILE}' 파일이 없습니다. 먼저 저장해주세요.")
        return

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        loaded = json.load(f)

    prompts.clear()
    prompts.extend(loaded)
    print(f"'{DATA_FILE}' 파일에서 {len(prompts)}개의 프롬프트를 불러왔습니다.")


def export_markdown():
    """전체 프롬프트를 카테고리별 Markdown 파일로 내보낸다(보너스1)."""
    print("\n=== Markdown 내보내기 ===")
    if not prompts:
        print("내보낼 프롬프트가 없습니다.")
        return

    os.makedirs(EXPORT_DIR, exist_ok=True)

    # 등장하는 카테고리별로 묶는다
    categories = []
    for p in prompts:
        if p["category"] not in categories:
            categories.append(p["category"])

    count = 0
    for category in categories:
        items = [p for p in prompts if p["category"] == category]
        # 파일명에 쓸 수 없는 공백은 밑줄로 치환
        filename = f"{category.replace(' ', '_')}.md"
        path = os.path.join(EXPORT_DIR, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# {category}\n\n")
            for p in items:
                mark = " ⭐" if p["favorite"] else ""
                f.write(f"## {p['title']}{mark}\n\n")
                f.write(f"{p['content']}\n\n")
        count += 1

    print(f"'{EXPORT_DIR}/' 폴더에 카테고리 {count}개의 Markdown 파일을 생성했습니다.")


def show_menu():
    """메인 메뉴를 출력한다."""
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("8. 프롬프트 수정")
    print("9. 프롬프트 삭제")
    print("10. 조회수 Top 목록")
    print("11. JSON으로 저장")
    print("12. JSON에서 불러오기")
    print("13. 카테고리별 Markdown 내보내기")
    print("0. 종료")


def main():
    """프로그램의 진입점. 메뉴를 반복 출력하고 입력을 처리한다."""
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "0":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break
        elif choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            show_favorites()
        elif choice == "8":
            edit_prompt()
        elif choice == "9":
            delete_prompt()
        elif choice == "10":
            show_top_viewed()
        elif choice == "11":
            save_to_json()
        elif choice == "12":
            load_from_json()
        elif choice == "13":
            export_markdown()
        else:
            print("잘못된 번호입니다. 메뉴에서 번호를 다시 선택해주세요.")


if __name__ == "__main__":
    main()
