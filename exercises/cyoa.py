"""Ask user for number, give hints about number if wrong."""


__author__ = "730557985"


points: int = 0
player: str = ""
X_EMOJI: str = "\U0000274C"


def main() -> None:
    """Overall game function for the coin-flip game."""
    global points
    playing: bool = True
    path_chosen: int = 0
    points = 0
    greet()
    while playing is True:
        print(f"You have {points} overall point(s)!")
        path_chosen = int(input(f"{player}, Enter the number for one of the following options: 1 = Play The Game! , 2 = Practice round?, 3 = End Experience. "))
        if path_chosen == 1:
            path1()
        if path_chosen == 2: 
            path2(0)
        if path_chosen == 3: 
            path3()
            playing = False
 

def greet() -> None:
    """Asks name then greets player to game."""
    global player
    player = input("What is your name? ")
    print(f"Welcome to the coin flip guessing game {player}")


def path1() -> None:
    """Number Guessing Game."""
    from random import randint
    secret: int = randint(1, 5)
    turn: int = 1
    global points
    print("You will have 3 turns to guess the secret number. You earn more points the less turns you use! ")
    while turn < 4:   
        guess: int = int(input(f"(Turn {turn}) Guess a number 1-5! "))
        if guess == secret and turn == 1:
            points += 3
            print("Correct on the first try! +3 points")
            turn = 4
        if guess == secret and turn == 2:
            points += 2
            turn = 4
            print("Correct on the second try! +2 points")
        if guess == secret and turn == 3:
            points += 1
            print("Correct on the last try! +1 point")
        if guess != secret:
            print(f"ERRRR, you couldn't be more wrong {X_EMOJI}{X_EMOJI}{X_EMOJI}")
        turn += 1
        if turn == 4:
            print(f"{player}, You are out of turns, please proceed to the main menu. ")


def path2(practice_points: int) -> int:
    """Number Guessing Game With Hints."""
    from random import randint
    secret: int = randint(1, 5)
    turn: int = 1
    while turn < 4:   
        guess: int = int(input(f"(Turn {turn}) Guess a number 1-5! "))
        if guess == secret and turn == 1:
            practice_points += 3
            print("Correct on the first try! +3 points")
            turn = 4
        if guess == secret and turn == 2:
            practice_points += 2
            print("Correct on the second try! +2 points")
            turn = 4
        if guess == secret and turn == 3:
            practice_points += 1
            print("Correct on the last try! +1 point")
        if guess != secret:
            print(f"ERRRR, you couldn't be more wrong {X_EMOJI}{X_EMOJI}{X_EMOJI}")
        turn += 1    
    print(f"{player}, You have earned {practice_points} point(s) in the practice round!")
    global points
    points += practice_points
    return points
    

def path3() -> None:
    """Ends Player Experience."""
    global points
    print(f"Goodbye! You have earned {points} point(s)!")


if __name__ == "__main__":
    main()