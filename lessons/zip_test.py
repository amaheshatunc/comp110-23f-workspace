"""Test my zip function!"""
__author__ = '730668496'
from lessons.zip import zip 


def test_empty_list() -> None:
    """This tests if the function still works if the length of one list is larger than the other."""
    colors: list[str] = ['red', 'blue']
    digits: list[int] = ['54']
    assert zip([colors, digits]) == {}


def test_one_element_list() -> None:
    """If both lists have an element, it should become a dictionary."""
    colors: list[str] = ['red']
    digits: list[int] = ['54']
    assert zip([colors, digits]) == {'red': 54}


def test_two_element_list() -> None:
    """If lists both have 2 elements, it should become a dictionary."""
    colors: list[str] = ['red', 'blue']
    digits: list[int] = ['54', '20']
    assert zip([colors, digits]) == {'red': 54, 'blue': 20}