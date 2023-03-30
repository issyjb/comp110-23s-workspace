"""EX07 - Dictionary Test."""


__author__ = "730557985"


from exercises.ex07.dictionary import invert, favorite_color, count


# invert tests
def test_normal_dict() -> None:
    """Use Case: Tests a dict with normal usage of strings."""
    test_dict: dict[str, str] = {'dog': 'cat'}
    assert invert(test_dict) == {'cat': 'dog'}


def test_int() -> None:
    """Use Case: Tests a dict made of ints."""
    test_dict: dict[str, str] = {'1': '2'}
    assert invert(test_dict) == {'2': '1'}


def test_empty() -> None:
    """Edge Case: Tests an empty dict."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


# favorite_color tests
def test_simple_colors() -> None:
    """Use Case: Tests a dict with normal names and colors provided."""
    test_dict: dict[str, str] = {'bob': 'blue', 'kate': 'pink', 'jim': 'blue'}
    assert favorite_color(test_dict) == "blue"


def test_repeats() -> None:
    """Use Case: Tests repeated values."""
    test_dict: dict[str, str] = {'bob': 'blue', 'bob': 'blue', 'bob': 'blue', 'bob': 'blue'}
    assert favorite_color(test_dict) == "blue"


def test_empty_dict() -> None:
    """Edge Case: Tests an empty dict."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ""


# count tests 
def test_() -> None:
    """Use Case: Tests a dict with normal values provided."""
    test_list: list[str] = ["dog", "cat", "dog", "cat", "bird", "pig"]
    assert count(test_list) == {'bird': 1, 'cat': 2, 'dog': 2, 'pig': 1}


def test_solo() -> None:
    """Use Case: Tests one given value."""
    test_list: list[str] = ["dog"]
    assert count(test_list) == {'dog': 1}


def test_empty_list() -> None:
    """Edge Case: Tests an empty list."""
    test_list: list[str] = []
    assert count(test_list) == {}