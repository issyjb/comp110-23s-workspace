"""EX09 - River Simulation."""

__author__ = "730557985"

from exercises.ex09.river import River

my_river: River = River(10, 2)

my_river.view_river()

my_river.remove_fish(2)