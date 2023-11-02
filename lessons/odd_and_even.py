def odd_and_even(list1: list[int]) -> list[int]:
        """Find the odd elements with even indexes."""
        i: int = 0
        list2: list[int] = []
 
        while i < len(list1):
            if list1[i] % 2 == 1 and i % 2 == 0:
                list2.append(list1[i])
            i += 1
 
        return list2

def odd_and_even1(list1: list[int]) -> list[int]:
        """Find the odd elements with even indexes."""
        i: int = 0
        list2: list[int] = []
 
        while i < len(list1):
            if list1[i] % 2 != 0 and i % 2 == 0:
                list2.append(list1[i])
            i += 1
 
        return list2


print(odd_and_even1([5,4,3,2,1,10,9,8]))
print(odd_and_even([5,4,3,2,1,10,9,8]))