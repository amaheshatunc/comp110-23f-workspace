"""EX07 - The one who tests all the time has nothing to test about except tests"""

__author__ = 730668496

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance

def test_invert_two_pairs() -> None:
    """This tests if the invert function inverts two key-value pairs."""
    dict1: dict[str, str] = {"Angelina" : "Jolee", "Bart" : "Petite"}
    assert invert(dict1) == {"Jolee" : "Angelina", "Petite" : "Bart"}


def test_invert_one_pair() -> None:
    """This tests if the invert function inverts one key-value pairs."""
    dict1: dict[str, str] = {"Angelina" : "Jolee"}
    assert invert(dict1) == {"Jolee" : "Angelina"}


def test_invert_empty_pair() -> None:
    """This tests if the invert function inverts a blank dictionary."""
    dict1: dict[str, str] = {}
    assert invert(dict1) == {}


def test_favorite_color_three_pair() -> None:
    """This tests if the favorite color function finds the favorite color of these individuals."""
    dict1: dict[str, str] = {"Angelina" : "Blue", "Filipe" : "Blue", "Burnemouth" : "Blue"}
    assert favorite_color(dict1) == "Blue"


def test_favorite_color_two_pair() -> None:
    """This tests if the favorite color function finds the favorite color of these two individuals."""
    dict1: dict[str, str] = {"Angelina" : "Green", "Reese" : "Blue"}
    assert favorite_color(dict1) == "Green"


def test_favorite_color_empty_pair() -> None:
    """This tests if the favorite color function finds the favorite color of these two individuals."""
    dict1: dict[str, str] = {}
    assert favorite_color(dict1) == ""


def test_count_two_words() -> None:
    """This tests if the count_two_words function finds the amount of times a name is called in a function."""
    list1: list[str] = ["Gojo", "Jogo", "Lelo", "Gojo", "Melo"]
    assert count(list1) == {"Gojo" : 2, "Jogo" : 1, "Lelo" : 1, "Melo" : 1}


def test_count_one_words() -> None:
    """This tests if the test_count_one_words function finds the amount of times a name is called in a function."""
    list1: list[str] = ["Gojo", "Jogo", "Lelo", "Melo"]
    assert count(list1) == {"Gojo" : 1, "Jogo" : 1, "Lelo" : 1, "Melo" : 1}


def test_count_empty_list() -> None:
    """This tests if the test_count_empty_list function finds the amount of times a name is called in a function with no names within it."""
    list1: list[str] = []
    assert count(list1) == {}


def test_alphabetizer_one_word() -> None:
    """This tests if the alphabetizer function finds the first letter of the list and finds other words equal to it."""
    list1: list[str] = ["Almond"]
    assert alphabetizer(list1) == {"A" : ["Almond"]}


def test_alphabetizer_two_word() -> None:
    """This tests if the alphabetizer function finds the first letter of the list and finds other words equal to it."""
    list1: list[str] = ["Almond", "Bistro"]
    assert alphabetizer(list1) == {"A" : ["Almond"], "B" : ["Bistro"]}


def test_alphabetizer_empty_list() -> None:
    """This tests if the alphabetizer function finds the first letter of the list and finds other words equal to it."""
    list1: list[str] = []
    assert alphabetizer(list1) == {}


def test_update_attendance_new_day() -> None:
    """This checks the attendance."""
    dictionary: dict[str, list[str]] = {"Monday": ["John"]}
    day: str = "Tuesday"
    people: str = "John"
    assert update_attendance(dictionary, day, people) == {"Monday" : ["John"], "Tuesday" : ["John"]}
    

def test_update_attendance_new_person() -> None:
    """This checks the attendance."""
    dictionary: dict[str, list[str]] = {"Monday": ["John"]}
    day: str = "Tuesday"
    people: str = "Finch"
    assert update_attendance(dictionary, day, people) == {"Monday": ["John"], "Tuesday": ["Finch"]}


def test_update_attendance_dupli() -> None:
    """This checks the attendance."""
    dictionary: dict[str, list[str]] = {"Monday": ["John", "Phil"], "Tuesday": ["John", "Brolie"]}
    day: str = "Tuesday"
    people: str = "John"
    assert update_attendance(dictionary, day, people) == {"Monday": ["John", "Phil"], "Tuesday": ["John", "Brolie"]}