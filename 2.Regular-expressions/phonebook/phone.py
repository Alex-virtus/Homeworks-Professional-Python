import re


def normalize_phone(phone: str) -> str:
    # Преобразуем телефон к формату +7(999)999-99-99 (доб.9999)
    pattern = re.compile(
        r"(\+7|8)\s*\(?(\d{3})\)?[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})(?:\s*\(?(доб.)\s*(\d+)\)?)?"
    )
    subst = r"+7(\2)\3-\4-\5 \6\7"
    return pattern.sub(subst, phone).strip()
