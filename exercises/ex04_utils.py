__author__ = "730668496"

def all(numbers: int, find: int) -> bool:
    rewind = 0
    if len(numbers) == 0:
        return False
        
    while (rewind < len(numbers)):
        # check if the find is equal to any number in the list
        if numbers[rewind] != find:
            return False
        rewind += 1
    return True

def max(input_list: list[int]) -> int:
    if len(input_list) == 0:
        raise ValueError("max() arg is an empty List")
    
    if len(input_list) == 1:
        return input_list[0]
    
    rewind: int = 0
    highest: int = input_list[0]    
    while (rewind < len(input_list)):
        if highest < input_list[rewind]:
            highest = input_list[rewind]
        rewind += 1
    return highest

def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    
    if len(list_one) != len(list_two):
        return False
    else:
        rewind: int = 0
        while rewind < len(list_one):
            if list_one[rewind] != list_two[rewind]:
                return False
            rewind += 1
    return True