"""Challenge Question 04 - Dict Function Writing."""

__author__ = "730557985"


def zip(str_list: list[str], int_list: list[int]) -> dict[str, int]:
    new_dict: dict = {}
    if len(str_list) != len(int_list):
            return new_dict
    else:
        idx: int = 0
        for item in str_list:
                new_dict[item] = int_list[idx]
                idx += 1
    return new_dict