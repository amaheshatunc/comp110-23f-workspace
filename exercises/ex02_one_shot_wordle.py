"""EX02 - Wordle that expects you to get it in one try."""

__author__ = "730668496"
word = "python"
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"
index: int = 0
final_line: str = ""
guess = str(input(f"What is your {len(word)}-letter guess? "))


while (len(guess) > len(word) or len(guess) < len(word)):    
    guess = str(input(f"That was not {len(word)} letters! Try again: "))


while index < (len(word)):
    if guess[index] == word[index]:
        final_line = final_line + green_box
    else:
        char_fake = False
        dif_i: int = 0
        while char_fake is False and dif_i < len(word):
            if word[dif_i] == guess[index]:
                char_fake = True
            else:
                dif_i = dif_i + 1
        if char_fake is True:
            final_line = final_line + yellow_box
        else:
            final_line = final_line + white_box
    index = index + 1
print(final_line) 
if guess == word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")