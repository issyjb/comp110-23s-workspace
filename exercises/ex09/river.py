"""File to define River class."""

__author__ = "730557985"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Defines river as a class."""
    
    #  attributes
    day: int
    bears: list
    fish: list

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of the animals to remove them if over the said age."""
        surviving_bears: list[Bear] = []
        surviving_fish: list[Fish] = []
        for item in self.fish:
            if item.age <= 3:
                surviving_fish.append(item)
        self.fish = surviving_fish
        for item in self.bears:
            if item.age <= 5:
                surviving_bears.append(item)
        self.bears = surviving_bears
        return None
    
    def remove_fish(self, amount: int):
        """Removes the amount of fish specified."""
        idx: int = 0
        while idx < amount:
            self.fish.pop(idx)
            idx += 1

    def bears_eating(self):
        """Removes fish as bear "eats" them."""
        for item in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                item.eat(3)
        return None
    
    def check_hunger(self):
        """Checks the hunger of the bear to see if still surviving."""
        surviving_bears: list[Bear] = []
        for item in self.bears:
            if item.hunger_score >= 0:
                surviving_bears.append(item)
        self.bears = surviving_bears
        return None
        
    def repopulate_fish(self):
        """Repopulates the number of fish."""
        offspring: int = (len(self.fish) // 2) * 4
        idx: int = 0
        while idx < offspring:
            self.fish.append("baby fish")
            idx += 1
        return None
    
    def repopulate_bears(self):
        """Repopulates the number of bears."""
        offspring: int = len(self.bears) // 2
        idx: int = 0
        while idx < offspring:
            self.bears.append("baby bear")
            idx += 1
        return None

    def view_river(self):
        """Prints out stats about the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self):
        """Simulates one week of life in the river."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()