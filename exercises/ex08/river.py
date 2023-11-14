"""File to define River class."""
__author__ = "730668496"


from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """The beginning of a river."""
    day: int
    bears: list[int]
    fish: list[int]

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
        """This will check the ages of the fish and bear."""
        alive_fish: list[Fish] = []
        alive_bear: list[Bear] = []

        for bear in self.bears:
            if bear.age <= 5:
                alive_bear.append(bear)
        
        for fish in self.fish:
            if fish.age <= 3:
                alive_fish.append(fish)

        self.bears = alive_bear
        self.fish = alive_fish
        return None
    
    def remove_fish(self, amount: int):
        """This removes a set amount of fish."""
        for _ in range(amount):
            self.fish.pop(0)
        return None

    def bears_eating(self):
        """This is the bears eating."""
        fish_count = len(self.fish) 
        for bear in self.bears: 
            if fish_count >= 5: 
                if fish_count >= 3: 
                    bear.eat(3) 
                    self.remove_fish(3) 
                    fish_count = len(self.fish) 
        return None

    def check_hunger(self):
        """This checks if the starved bears are dead or not."""
        alive_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                alive_bears.append(bear)
        self.bears = alive_bears
        
    def repopulate_bears(self):
        """This repopulates the fish in the river."""
        new_Bears = len(self.bears) // 2
        for _ in range(new_Bears):
            self.bears.append(Bear())
        return None 
    
    def repopulate_fish(self):
        """This repopulates the bear in the river."""
        new_Fish = (len(self.fish) // 2) * 4
        for _ in range(new_Fish):
            self.fish.append(Fish())
        return None
    
    def view_river(self):
        """Prints river attributes."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
            
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
        """Simulate one week of life in the river."""
        for _ in range(7):
            self.day += 1
        return self.day