"""EX05 - Utils File."""


__author__ = "730557985"


def only_evens(int_list: list[int]) -> list:
    """Analyzes given list and returns even ints."""
    answer_list: list[int] = list()
    for item in int_list:
        if item % 2 == 0:
            answer_list.append(item)
    return answer_list


def concat(int_list1: list[int], int_list2: list[int]) -> list:
    """Adds two lists together."""
    combined_list: list[int] = list()
    for item in int_list1:
        combined_list.append(item)
    for item in int_list2:
        combined_list.append(item)
    return combined_list


def sub(int_list: list[int], idx_1: int, idx_2: int) -> list:
    """Generates list between the two specified index points."""
    ranged_list: list[int] = list()
    if idx_1 < 0:
        idx_1 = 0
    if idx_2 > len(int_list):
        idx_2 = len(int_list)
    if len(int_list) == 0 or idx_1 >= len(int_list) or idx_2 <= 0:
        return ranged_list
    else: 
        for idx in range(idx_1, idx_2):
            ranged_list.append(int_list[idx])
        return ranged_list