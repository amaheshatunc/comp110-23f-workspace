"""File to define Fish class."""


class Fish:
    """This is the beautiful looking class."""
    age: int 

    def __init__(self):
        """Constructor."""
        self.age = 0
        return None
    
    def one_day(self):
        """Simulates one day."""
        self.age += 1
        return None