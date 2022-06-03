import constants
import time
from random import randint
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.balls import Ball

class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score = cast.get_first_actor("scores")
        ball = cast.get_first_actor("balls")
        player = cast.get_first_actor("players")
        segments = player.get_segments()
        messages = cast.get_actors("messages")
        new_balls = cast.get_actors("balls")

        self._video_service.clear_buffer()
        self._video_service.draw_actor(ball)
        self._video_service.draw_actors(segments)
        self._video_service.draw_actors(new_balls)
        self._video_service.draw_actor(score)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()

    def _activate_ball(self, cast):
        ball = cast.get_first_actor("balls")
        ball.release()

    