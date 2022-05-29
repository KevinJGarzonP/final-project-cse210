from game.casting.actor import Actor
from game.shared.point import Point


class Ball(Actor):
    """
    A round obstacle that falls through the screen trying to collide with the player.
    
    The responsibility of Ball is to appear at the top of the scenario, .

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        "Constructs a new Food."