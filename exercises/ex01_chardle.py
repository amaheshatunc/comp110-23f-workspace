"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730668496"

word_input: str = input("Enter a 5-character word: ")

if len(word_input) != 5:
    print("Error: Word must contain 5 characters")
    exit()

character_input: str = input("Enter a single character: ")
if len(character_input) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + character_input + " in " + word_input)

match_counter: int = 0

if word_input[0] == character_input:
    print(character_input + " found at index 0")
    match_counter = match_counter + 1

if word_input[1] == character_input:
    print(character_input + " found at index 1")
    match_counter = match_counter + 1

if word_input[2] == character_input:
    print(character_input + " found at index 2")
    match_counter = match_counter + 1
    
if word_input[3] == character_input:
    print(character_input + " found at index 3")
    match_counter = match_counter + 1

if word_input[4] == character_input:
    print(character_input + " found at index 4")
    match_counter = match_counter + 1

if match_counter > 1:
    print(str(match_counter) + " instances of " + character_input + " found in " + word_input)
elif match_counter == 1:
    print(str(match_counter) + " instance of " + character_input + " found in " + word_input)
else:
    print("No instances of " + character_input + " foudn in " + word_input)