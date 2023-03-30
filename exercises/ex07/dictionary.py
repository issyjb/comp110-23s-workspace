"""EX07 - Dictionary."""


__author__ = "730557985"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of inputted dictionary."""
    dict2: dict[str, str] = {}
    for key in dict1:
        if dict1[key] in dict2:
            raise KeyError("KeyError: Repeated keys.")
        else:
            dict2[dict1[key]] = key
    return dict2


def favorite_color(dict1: dict[str, str]) -> str:
    """Returns the favorite color that appears most."""
    dict2: dict[str, int] = {}
    common_color: str = ""
    count: int = 0
    for name in dict1:
        if dict1[name] in dict2:
            dict2[dict1[name]] += 1
        else:
            dict2[dict1[name]] = 1
    for color in dict2:
        if dict2[color] > count:
            count = dict2[color]
            common_color = color
    return common_color


def count(values: list[str]) -> dict[str, int]:
    """Produces dictionary with count of number of times the values appear."""
    result: dict[str, int] = {}
    for item in values:
        result[item] = 0
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result