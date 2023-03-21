"""Ask user for number, give hints about number if wrong."""


__author__ = "730557985"


points: int = 0
player: str = input("What is your name? ")
path_chosen: int = input(f"Hi, {player} Enter the number for one of the following options: 1 = Play Solo! , 2 = Play with Hints!, 3 = End Experience. ")


def main() -> None:
    """Overall game function for the coin-flip game."""
    greet()
    global path_chosen
    if path_chosen == 1:
        path1()
    if path_chosen == 2: 
        path2()
    if path_chosen == 2: 
        path3()


def greet() -> None:
    """Asks name then greets player to game."""
    global player
    print(f"Welcome to the coin flip guessing game {player}")

def path1(guess: int, SECRET: int) -> int:
    """Number Guessing Game."""
    from random import randint
    SECRET: int = randint(1, 10)
    guess: int = input("Guess a number 1-10! ")
    turn: int = 0
    global points
    while turn < 10:   
        if guess == SECRET:
            points += 1
            print("Correct! + 1 point")
        else:
            print("ERRRR, you couldn't be more wrong")
        turn += 1        
    return points


def path2(guess: int, SECRET: int) -> int:
    """Number Guessing Game With Hints."""
    from random import randint
    SECRET: int = randint(1, 10)
    guess: int = input("Guess a number 1-10! ")
    turn: int = 0
    global points
    while turn < 10:   
        if guess == SECRET:
            points += 1
            print("Correct! + 1 point")
            
        else: 
            if guess % 2 == 1:
                print("Your guess is odd. The answer is even. ")
            if guess < SECRET:
                print("Too low! ")
            else:
                print("Too high! ")
            guess = int(input("Wrong guess. Try again! "))
        turn += 1
    return points


def path3() -> None:
    """Ends Player Experience."""
    global points
    print(f"Goodbye! You have earned {points} points!")


if __name__ == "__main__":
    main()