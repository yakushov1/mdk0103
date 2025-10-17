def reverse_string(s: str) -> str:
    """Возвращает инвертированную строку"""
    return s[::-1]


def count_words(text):
    """Считает количество слов в строке"""
    words = text.split()
    return len(words)
