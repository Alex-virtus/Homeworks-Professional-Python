import re


def contains_keywords(text: str, keywords: list) -> bool:
    text = text.lower()
    return any(re.search(rf'\b{kw}\b', text, re.IGNORECASE) for kw in keywords)
