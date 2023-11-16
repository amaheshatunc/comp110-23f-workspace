"""This is the start of everything."""
from exercises.ex08.river import River

my_river: River = River(10, 2)
my_river.view_river()
my_river.one_river_week()
my_river.remove_fish(1)
my_river.repopulate_bears()
my_river.one_river_week()