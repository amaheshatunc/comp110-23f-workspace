"""Test my zip function!"""

__author__ = "730668496"

from lessons.zip import zip 


def test_different_len_list() -> None:
    """This tests if the function still works if the length of one list is larger than the other."""
    strings: list[str] = ["red", "blue"]
    numbers: list[int] = [54]
    assert zip(strings, numbers) == {}


def test_one_element_list() -> None:
    """If both lists have an element, it should become a dictionary."""
    strings: list[str] = ["red"]
    numbers: list[int] = [54]
    assert zip(strings, numbers) == {'red': 54}


def test_two_element_list() -> None:
    """If lists both have 2 elements, it should become a dictionary."""
    strings: list[str] = ["red", "blue"]
    numbers: list[int] = [54, 20]
    assert zip(strings, numbers) == {'red': 54, 'blue': 20}