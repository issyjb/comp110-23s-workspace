"""File to define Bear class."""

__author__ = "730557985"


class Bear:
    """Defines Bear as a class."""

    # attributes
    age: int
    hunger_score: int 
    
    def __init__(self):
        """Intializes self attributes."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Alters attributes for the course of one day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Allows the bear to eat fish and alter hunger score."""
        self.hunger_score += num_fish
        return None