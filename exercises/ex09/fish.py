"""File to define Fish class."""

__author__ = "730557985"


class Fish:
    """Defines Fish as a class."""
    
    # attributes
    age: int

    def __init__(self):
        """Intializes self attributes."""
        self.age = 0
        return None
    
    def one_day(self):
        """Alters attributes for the course of one day."""
        self.age += 1
        return None