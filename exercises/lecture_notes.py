"""
HOW I MADE THE CODE WAS HORRIBLY WRONG

def mimic_letter(my_words: str, letter_idx: int):
    my_words = print(my_words, letter_idx)
    return my_words


my_words: str = str(input("Type whatever you want to type!"))
letter_idx: int = int(input("What index do you want to print out?"))
print(mimic_letter) """

def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index `letter_idx"""
    if letter_idx >= len(my_words):
        return ("Index too high")
    #if we made it this far then that means the letter_idx is valid
    return my_words[letter_idx]

my_words: str = str(input("Type whatever you want to type!"))
letter_idx: int = int(input("What index do you want to print out?"))
print(mimic_letter(my_words,letter_idx))
