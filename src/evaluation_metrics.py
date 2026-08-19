from collections import Counter


def token_f1(prediction: str, reference: str) -> float:
    """
    Calculate token-level F1 between a model prediction
    and a reference answer.
    """
    prediction_tokens = prediction.lower().split()
    reference_tokens = reference.lower().split()

    if not prediction_tokens or not reference_tokens:
        return 0.0

    prediction_counts = Counter(prediction_tokens)
    reference_counts = Counter(reference_tokens)

    overlap = sum(
        (prediction_counts & reference_counts).values()
    )

    if overlap == 0:
        return 0.0

    precision = overlap / len(prediction_tokens)
    recall = overlap / len(reference_tokens)

    return 2 * precision * recall / (precision + recall)


def exact_match(prediction: str, reference: str) -> bool:
    """Check whether two answers match after normalization."""
    return (
        prediction.strip().lower()
        == reference.strip().lower()
    )


def evaluate_response(
    prediction: str,
    reference: str
) -> dict:
    """Return evaluation metrics for one model response."""
    return {
        "exact_match": exact_match(
            prediction,
            reference
        ),
        "token_f1": round(
            token_f1(prediction, reference),
            4
        ),
    }
