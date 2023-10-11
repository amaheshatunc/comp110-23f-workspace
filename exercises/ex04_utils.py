__author__ = "730668496"

def all(numbers: int, find: int) -> bool:
    rewind = 0    
    while rewind < len(numbers):
        # check if the find is equal to any number in the list
        if numbers[rewind] == find:
            return True
        rewind += 1
    return False

def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    rewind = 0
    highest = input[0]

    if len(input) == 1:
        return input[0]
    
    while rewind < len(input):
        if input[rewind] > highest:
            highest = input[rewind]
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