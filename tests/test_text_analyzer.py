from src.text_analyzer import tokenize


def test_tokenize():
    text = "Hello world! This is a test."
    tokens = tokenize(text)

    assert tokens == ["Hello", "world!", "This", "is", "a", "test."]
