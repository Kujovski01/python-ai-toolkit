from .text_analyzer import tokenize


def text_statistics(texts: list[str]) -> dict:
    """Calculate basic statistics for a collection of texts."""
    if not texts:
        return {
            "documents": 0,
            "total_words": 0,
            "average_words": 0.0,
            "longest_document": 0,
            "shortest_document": 0,
        }

    word_counts = [len(tokenize(text)) for text in texts]

    return {
        "documents": len(texts),
        "total_words": sum(word_counts),
        "average_words": round(
            sum(word_counts) / len(word_counts),
            2,
        ),
        "longest_document": max(word_counts),
        "shortest_document": min(word_counts),
    }
