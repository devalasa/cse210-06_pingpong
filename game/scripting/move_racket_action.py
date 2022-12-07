from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveRacketAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(RACKET_GROUP)
        body = racket.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        y = position.get_y()
        position = position.add(velocity)

        if y < 0:
            position = Point(position.get_x(), 0 )
        elif y > (SCREEN_HEIGHT - RACKET_HEIGHT):
            position = Point(position.get_x(), SCREEN_HEIGHT - RACKET_HEIGHT)
        body.set_position(position)

        #Code for the second racket
        racket2 = cast.get_actors(RACKET_GROUP)[1]
        body2 = racket2.get_body()
        velocity2 = body2.get_velocity()
        position2 = body2.get_position()
        y2 = position2.get_y()
        position2 = position2.add(velocity2)

        if y2 < 0:
            position2 = Point(0, position2.get_x())
        elif y2 > (SCREEN_HEIGHT - HUD_MARGIN -  RACKET_HEIGHT):
            position2 = Point(position2.get_x(), SCREEN_HEIGHT - RACKET_HEIGHT)
        body2.set_position(position2)



        

