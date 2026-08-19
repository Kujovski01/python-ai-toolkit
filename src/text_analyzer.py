import re
from collections import Counter


def tokenize(text: str) -> list[str]:
    """Convert text into lowercase word tokens."""
    return re.findall(r"\b\w+\b", text.lower())


def word_count(text: str) -> int:
    """Return the number of words in a text."""
    return len(tokenize(text))


def vocabulary(text: str) -> set[str]:
    """Return the unique words appearing in the text."""
    return set(tokenize(text))


def most_common_words(
    text: str,
    n: int = 10
) -> list[tuple[str, int]]:
    """Return the n most frequent words."""
    return Counter(tokenize(text)).most_common(n)
