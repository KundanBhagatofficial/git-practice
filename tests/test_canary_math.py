from canary_math import increment


def test_increment_returns_next_integer() -> None:
    assert increment(1) == 2
    assert increment(-1) == 0
