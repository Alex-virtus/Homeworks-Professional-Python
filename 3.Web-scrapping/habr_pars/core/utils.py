def contains_keywords(text: str, keywords: list) -> bool:
    text = text.lower()
    return any(word in text for word in keywords)
