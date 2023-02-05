"""EX 02 - One Shot Wordle."""

__author__ = "730557985"

SECRET: str = "python"
word_inputted: str = input(f"What is your {len(SECRET)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index_search: int = 0
emoji_string: str = ""
found_elsewhere: bool = False
alternate_index: int = 0

# prompts to input the correct length of word
while len(word_inputted) != len(SECRET):
    word_inputted = input(f"That was not {len(SECRET)} letters! Try again: ")

# provides correct emoji colors to produce string
while index_search < len(SECRET):
    if word_inputted[index_search] == SECRET[index_search]:
        emoji_string = emoji_string + GREEN_BOX
    else:
        while found_elsewhere is False and alternate_index < len(SECRET):
            if word_inputted[index_search] == SECRET[alternate_index]:
                found_elsewhere = True
                emoji_string = emoji_string + YELLOW_BOX
            else:
                alternate_index = alternate_index + 1
                
        if found_elsewhere is False:
            emoji_string = emoji_string + WHITE_BOX
    index_search = index_search + 1
    alternate_index = 0
    found_elsewhere = False
    
print(emoji_string)

# informs if they guessed word correctly
if word_inputted == SECRET:
    print("Woo! You got it! ")
else: 
    print("Not quite. Play again soon! ")
