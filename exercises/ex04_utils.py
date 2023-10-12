"""EX04 - list utility functions (fun!)!"""
__author__ = "730668496"


def all(numbers: list[int], find: int) -> bool:
    """This will check if the number is within the list or not."""
    rewind: int = 0
    if len(numbers) == 0:
        return False
        
    while (rewind < len(numbers)):
        """"Check if the find is equal to any number in the list."""
        if numbers[rewind] != find:
            return False
        """This checks if the find is equal to any number in the list."""
        rewind += 1
    return True


def max(input_list: list[int]) -> int:
    """This function returns the maximum number in a list."""
    if len(input_list) == 0:
        raise ValueError("max() arg is an empty List")
    
    if len(input_list) == 1:
        return input_list[0]
    
    rewind: int = 0
    highest: int = input_list[0]    
    while (rewind < len(input_list)):
        """This function will return the highest number in a list."""
        if highest < input_list[rewind]:
            highest = input_list[rewind]
        rewind += 1
    return highest


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """This function will check if two lists are equal."""
    if len(list_one) != len(list_two):
        return False
    else:
        rewind: int = 0
        while rewind < len(list_one):
            if list_one[rewind] != list_two[rewind]:
                return False
            rewind += 1
    return True