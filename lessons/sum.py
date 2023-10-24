"""Summing the elements of a list using different loops."""
__author__ = "730668496"


def w_sum(vals: list[float]) -> float:
    """Adds the list."""
    if len(vals) == 0:
        return 0.0
    else:
        index = 0
        total = 0.0
        while index < len(vals):
            total += vals[index]
            index += 1
        return total


def f_sum(vals: list[float]) -> float:
    """Adds the list in another way."""
    index = 0.0
    for n in vals:
        index += n
    return index


def f_range_sum(vals: list[float]) -> float:
    """Adds the list in even better another way."""
    index = 0.0    
    for n in range(0, len(vals)):
        index = index + vals[n]
    return index    