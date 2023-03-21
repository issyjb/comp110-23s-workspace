"""Example function for unit tests"""

def oldsum(xs: list [float]) -> float:
    """return sum of all elements in xs with while loop"""
    sum_total: float = 0.0
    idx: int = 0
    while idx < len (xs) :
        sum_total += xs [idx]
        idx += 1
    return sum_total

def sum(xs: list[float]) -> float:
    """return sum of all elements in xs with for loop and range"""
    sum_total: float = 0.0
    for item in xs:
        sum_total += item
    for idx in range(0, len(xs)):
        print (f"{idx}: {xs[idx]}")
    return sum_total

