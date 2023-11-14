"""File to define Bear class."""


class Bear:
    """This is the beautiful looking class."""
    age: int 
    hunger_score: int 

    def __init__(self):
        """Constructor."""
        self.age = 0
        self.hunger_score = 0 
        return None
        
    def one_day(self):
        """This tracks the day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """This makes the Bear eat."""
        self.hunger_score += num_fish
        return None