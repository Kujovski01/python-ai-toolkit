from src.dataset_statistics import text_statistics


def test_text_statistics():
    texts = [
        "hello world",
        "this is a test",
    ]

    stats = text_statistics(texts)

    assert stats["documents"] == 2
    assert stats["total_words"] == 6
    assert stats["average_words"] == 3.0
    assert stats["longest_document"] == 4
    assert stats["shortest_document"] == 2


def test_text_statistics_empty():
    stats = text_statistics([])

    assert stats["documents"] == 0
    assert stats["total_words"] == 0
    assert stats["average_words"] == 0.0
