"""EX01 - Chardle - A cute step toward World."""

__author__ = "730557985"

word_inputted: str = input("Enter a 5-character word: ")

if (len(word_inputted) != 5):
    print("Error: Word must contain 5 characters")
    print(exit())

letter_inputted: str = input("Enter a single character: ")
if (len(letter_inputted) != 1):
    print("Error: Character must be a single character")
    print(exit())
    
print("Searching for " + letter_inputted + " in " + word_inputted)
letter_count: int = 0

if (word_inputted[0] == letter_inputted):
    print(letter_inputted + " found at index 0")
    letter_count = (letter_count + 1)

if (word_inputted[1] == letter_inputted):
    print(letter_inputted + " found at index 1")
    letter_count = (letter_count + 1)
if (word_inputted[2] == letter_inputted):
    print(letter_inputted + " found at index 2")
    letter_count = (letter_count + 1)
if (word_inputted[3] == letter_inputted):
    print(letter_inputted + " found at index 3")
    letter_count = (letter_count + 1)
if (word_inputted[4] == letter_inputted):
    print(letter_inputted + " found at index 4")
    letter_count = (letter_count + 1)

if letter_count == 0:
    print("No instances of " + letter_inputted + " found in " + word_inputted)
if letter_count == 1:
    print("1 instance of " + letter_inputted + " found in " + word_inputted)
if int(letter_count) > 1:
    print(str(letter_count) + " instances of " + letter_inputted + " found in " + word_inputted)
