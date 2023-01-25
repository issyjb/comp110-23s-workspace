"""EX01 - Chardle - A cute step toward World"""

__author__ = "730557985"

word_inputted: str = input("Enter a 5-character word: ")
letter_inputted: str = input("Enter a single character: ")
print("Searching for " + letter_inputted + " in " + word_inputted)
count: int = 0

if (word_inputted[0] == letter_inputted):
    print(letter_inputted + " found at index 0")
    count == (count + 1)
if (word_inputted[1] == letter_inputted):
    print(letter_inputted + " found at index 1")
    count == (count + 1)
if (word_inputted[2] == letter_inputted):
    print(letter_inputted + " found at index 2")
    count == (count + 1)
if (word_inputted[3] == letter_inputted):
    print(letter_inputted + " found at index 3")
    count == (count + 1)
if (word_inputted[4] == letter_inputted):
    print(letter_inputted + " found at index 4" )
    count == (count + 1)

print("There are " + str(count) + " instances of " + letter_inputted)

if count == 0:
    print("No instances of " + letter_inputted + " found in " + word_inputted)