__author__ = "730668496"

def contains_char(search_string: str, single_char: str) -> bool:
    assert len(single_char) == 1
    index: int = 0
    """If search_string contains any letters from single_char then it will return true, otherwise it will return false. This is checking if any letters are matching anywhere in search_string."""
    while index < len(search_string):
        if single_char == search_string[index]:
            return True
        index += 1
    return False

def emojified(guess: str, secret_guess: str) -> str:
    """functions returns emojis depending if they wrong, right or close to the correct answer"""
    assert len(guess) == len(secret_guess)
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    empty_str: str = ""
    index: int = 0
    while index < len(secret_guess):
        if guess[index] == secret_guess[index]:
            empty_str = empty_str + green_box
        elif contains_char(secret_guess, guess[index]):
            empty_str = empty_str + yellow_box
        else:
            empty_str = empty_str + white_box
        index += 1
    return empty_str

def input_guess(expected_length: int) -> str:
    """Function makes user input his guess to see if they are right or wrong."""
    guess_word: str = input(f"Enter a {expected_length} character word: ")
    while expected_length != len(guess_word):
        guess_word = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess_word

def main() -> None:
    """This function allows for the game to be played, tracks the user input and prompts the user to play for a few more turns before the game stops."""
    secret_word: str = "python"
    counter = 1
    win = False
    while counter < 7 and win is False:
        print(f"=== Turn {counter}/6 ===")
        guess_word = input_guess(len(secret_word))
        print(emojified(guess_word, secret_word))
        if guess_word == secret_word:
            win = True
        else:
            counter += 1
    if win is True:
        print(f"You won in {counter}/6 turns!")
    else: 
        print("X/6 - Sorry, try again tomorrow ")

if __name__ == "__main__":
    main()

