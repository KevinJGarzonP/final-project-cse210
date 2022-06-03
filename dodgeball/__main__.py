import constants
import threading
import time
import random

from game.casting.cast import Cast
from game.casting.balls import Ball
from game.casting.score import Score
from game.casting.player import Player
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.move_ball_action import MoveBallAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point



def main():
    # create the cast
    cast = Cast()
    cast.add_actor("balls", Ball())
    cast.add_actor("players", Player())
    cast.add_actor("scores", Score())
    
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", MoveBallAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))   
    
    director = Director(video_service)
    director.start_game(cast, script)

    def add_ball(self, cast):
            while True:
                x = random.randint(0, constants.MAX_X)
                y = random.randint(0, constants.MAX_Y)
                position = Point(x, y)
                new_ball = Ball()
                new_ball.set_position(position)
                cast.add_actor("balls", new_ball)
                time.sleep(5)

    add_new_ball = threading.Thread(target=add_ball)
    add_new_ball.start()

if __name__ == "__main__":
    main()