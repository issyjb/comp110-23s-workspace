"""EX05 - Utils Test."""


__author__ = "730557985"


from exercises.ex05.utils import only_evens, sub, concat


def test_mixture() -> None:
    """Tests a list with mixed odds and evens."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(test_list) == [2, 4, 6]


def test_negatives() -> None:
    """Tests a list with negative ints."""
    test_list: list[int] = [-1, -2, -3, -4]
    assert only_evens(test_list) == [-2, -4]


def test_onlyodds() -> None:
    """Tests a list with only odds."""
    test_list: list[int] = [1, 3, 5]
    assert only_evens(test_list) == []


def test_odds_and_evens() -> None:
    """Tests odds and evens."""
    test_list1: list[int] = [1, 3, 5]
    test_list2: list[int] = [2, 4, 6]
    assert concat(test_list1, test_list2) == [1, 3, 5, 2, 4, 6]


def test_pos_and_neg() -> None:
    """Tests positive and negative lists."""
    test_list1: list[int] = [1, 3, 5]
    test_list2: list[int] = [-1, -3, -5]
    assert concat(test_list1, test_list2) == [1, 3, 5, -1, -3, -5]


def test_one_empty() -> None:
    """Tests one empty list with one regular."""
    test_list1: list[int] = [1, 3, 5]
    test_list2: list[int] = []
    assert concat(test_list1, test_list2) == [1, 3, 5]


def test_small_range() -> None:
    """Tests a small range."""
    test_list: list[int] = [1, 3, 5]
    test_idx1: int = 1
    test_idx2: int = 2
    assert sub(test_list, test_idx1, test_idx2) == [3]


def test_large_range() -> None:
    """Tests a large range."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_idx1: int = 3
    test_idx2: int = 6
    assert sub(test_list, test_idx1, test_idx2) == [4, 5, 6]


def test_0_range() -> None:
    """Tests an empty range."""
    test_list: list[int] = [1, 3, 5]
    test_idx1: int = 0
    test_idx2: int = 0
    assert sub(test_list, test_idx1, test_idx2) == []