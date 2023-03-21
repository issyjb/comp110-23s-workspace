"""EX04 - List Utils."""


__author__ = "730557985"


def all(int_list: list[int], given_int: int) -> bool:
    """Sees if given integer is found in list."""
    idx: int = 0
    status: bool = False
    if len(int_list) == 0:
        status = False
    while idx < len(int_list):
        if given_int != int_list[idx]:
            status = False
            return False
        else: 
            status = True
        idx += 1
    return status


def max(input: list[int]) -> int:
    """Finds largest integer in list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List.")
    current_int: int = 0
    largest_int: int = 0
    while current_int < len(input):
        if input[current_int] > input[largest_int]:
            largest_int = current_int
        current_int += 1
    return input[largest_int]


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Sees if two lists are equivalent."""
    if list1 == list2:
        return True
    else:
        return False