import random
from constants import *
from game.casting.actor import Actor
from game.shared.point import Point


class Ball(Actor):
    """
    A round obstacle that falls through the screen trying to collide with the player.
    
    The responsibility of Ball is to appear at the top of the scenario, .

    Attributes:
        _points (int): The number of points the ball is worth.
    """
    def __init__(self):
        "Constructs a new Ball."
        super().__init__()
    
    def bounce_x(self):
        """Bounces the ball in the x direction."""
        velocity = self._body.get_velocity()
        rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x() * rn * -1
        vy = velocity.get_y()
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def bounce_y(self):
        """Bounces the ball in the y direction."""
        velocity = self._body.get_velocity()
        rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x()
        vy = velocity.get_y() * rn * -1 
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def release(self):
        """Release the ball in a random direction."""
        rn = random.uniform(0.9, 1.1)
        vx = random.choice([-BALL_VELOCITY * rn, BALL_VELOCITY * rn])
        vy = -BALL_VELOCITY
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)
