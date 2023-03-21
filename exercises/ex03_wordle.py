"""EX03 - Wordle - A more structured wordle."""

__author__ = "730557985"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(wordstring: str, characterstring: str) -> bool:
    """Evaluates if single character of second string is found in any index of the first"""
    assert len(characterstring) == 1
    index_search: int = 0
    while index_search < len(wordstring):
        if characterstring == wordstring[index_search]:
            return True
        else:
            index_search = index_search + 1
    return False

def emojified(guess: str, secret: str) -> str:
    """Assigns emoji boxes in correlation to if a character is found in the word"""
    assert len(guess) == len(secret)
    index_search: int = 0
    emoji_string: str = ""
    while index_search < len(secret):
        if guess[index_search] == secret[index_search]:
            emoji_string = emoji_string + GREEN_BOX
        else:
            not_green: bool = contains_char(secret, guess[index_search])
            if not_green == True:
                emoji_string = emoji_string + YELLOW_BOX
            else:
                emoji_string = emoji_string + WHITE_BOX
        index_search = index_search + 1
    return emoji_string

def input_guess(expected_length: int) -> str:
    word_inputted: str = input(f"Enter a {expected_length} character word: ")
    while len(word_inputted) != expected_length:
        word_inputted = input(f"That wasn't {expected_length} chars! Try again: ")
    return word_inputted

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn: int = 1
    while turn <= 6:
        print(f"===Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns! ")
            turn = 7
        else: 
            turn = turn + 1
    if guess != secret:
       print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()