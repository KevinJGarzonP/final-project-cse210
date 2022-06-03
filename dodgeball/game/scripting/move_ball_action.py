from constants import *
from game.scripting.action import Action


class MoveBallAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script):
        ball = cast.get_first_actor("balls")
        position = ball.get_position()
        velocity = ball.get_velocity()
        position = position.add(velocity)
        ball.set_position(position)
