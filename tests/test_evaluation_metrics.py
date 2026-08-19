from src.evaluation_metrics import token_f1


def test_token_f1_exact_match():
    assert token_f1("hello world", "hello world") == 1.0


def test_token_f1_partial_match():
    score = token_f1("hello there", "hello world")
    assert 0.0 < score < 1.0


def test_token_f1_no_match():
    assert token_f1("hello", "goodbye") == 0.0
