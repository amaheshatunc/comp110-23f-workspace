"""CQ07 - a masterpiece. 'Mutations are a common happenstance in this field of work.'- Some character in some video game."""
from __future__ import annotations
__author__ = "730668496"


class Point:
    """This is the beautiful looking class."""
    x: float 
    y: float 

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Beautiful looking Constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """This method mutates a point."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """This method creates an entirely new point."""
        self.x * factor
        self.y * factor
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self) -> str:
        """This turns stuff into strings."""
        new_point: str = f"x: {self.x}; y: {self.y}"
        return new_point
    
    def __mul__(self, factor: int | float) -> Point:
        """This fancy lil thing multiplies stuff."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
        
    def __add__(self, value: int | float) -> Point: 
        """If you need to add the points up just put it here."""
        new_point: Point = Point(self.x + value, self.y + value)
        return new_point