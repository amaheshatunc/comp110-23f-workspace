"""Making a beautiful dictionary in this dictionaryless world."""
__author__ = 730668496


def invert(inp_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the dictionary."""
    key_wrong: bool = False
    for key in inp_dict:
        repeat: int = 0
        for nestedkey in inp_dict:
            """This nested for loop checks if any of the other (yet to be inverted) values have the same values by comparing it key with the nestedkey value (the nested value continously changes with each loop)."""
            if (inp_dict[key] == inp_dict[nestedkey]):
                repeat += 1
                """This loop helps check if the nestkey and key are always comparing new keys."""
            if (repeat > 1):
                key_wrong = True
        """Repeats the check."""
        repeat = 0

    """Raises the KeyError."""
    if key_wrong is True: 
        raise KeyError("Too many same keys in dictionaries, change them.")

    blank_dict: dict[str, str] = {}
    for key in inp_dict:
        blank_dict[inp_dict[key]] = key
    return blank_dict


def favorite_color(inp_dict: dict[str, str]) -> str:
    """This gives out the favorite color."""
    blank_dict: dict[str, int] = {}
    max_color = 0
    pop_color: str = ""

    for name in inp_dict:
        color = inp_dict[name]
        if color in blank_dict:
            blank_dict[color] += 1
        else:
            blank_dict[color] = 1

        if blank_dict[color] > max_color or (blank_dict[color] == max_color and color == pop_color):
            max_color = blank_dict[color]
            pop_color = color

    return pop_color


def count(word_list: list[str]) -> dict[str, int]:
    """Theres a list that creates a dictionary and counts the value of the number."""
    blank_dict: dict[str, int] = {}
    for name in word_list:
        if name in blank_dict:
            blank_dict[name] += 1
        else: 
            blank_dict[name] = 1
    return blank_dict


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """Check the first letter of the words and check with everything else."""
    new_dict: dict[str, list[str]] = {}
    blank_list: list[str] = []
    for word in list1: 
        first_letter = word[0]
        blank_list.append(word)
        if first_letter in list1:
            new_dict[first_letter].append(blank_list)
        else: 
            new_dict[first_letter] = [word]
    return new_dict


def update_attendance(dictionary: dict[str, list[str]], day: str, people: str) -> dict[str, list[str]]:
    """Changes the dictionary to check if student was marked as present on the attendance log."""
    if day in dictionary:
        dictionary[day].append(people)
    else:
        dictionary[day] = [people]
    return dictionary