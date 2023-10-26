"""Making two ists into a dictionary."""
__author__ = '730668496'


def zip(strings: list[str], numbers: list[int]) -> dict[str, int]:
    """Takes two list and returns it in dictionary format."""
    dictionary_extra: dict[str,int] = {}
    if len(strings) != len(numbers):
        return dictionary_extra
    for i in range(0, len(strings)):
        dictionary_extra[strings[i]] = numbers[i]
    return dictionary_extra