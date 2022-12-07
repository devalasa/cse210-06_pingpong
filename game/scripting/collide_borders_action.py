from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        body = ball.get_body()
        scores = cast.get_first_actor(SCORE_STATS_GROUP)
        score1 = scores.get_score(1)
        score2 = scores.get_score(2)
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        bounce_sound = Sound(BOUNCE_SOUND)

        if (score1 < MAXIMUM_LIVES) and (score2 < MAXIMUM_LIVES):
            if x < FIELD_LEFT:
                ball.bounce_x()
                scores.add_score(2)
                callback.on_next(CONTINUE)

            elif x >= (FIELD_RIGHT-BALL_WIDTH):
                ball.bounce_x()
                scores.add_score(1)
                callback.on_next(CONTINUE)

            if y < FIELD_TOP:
                ball.bounce_y()
                self._audio_service.play_sound(bounce_sound)

            elif y >= (FIELD_BOTTOM-BALL_HEIGHT):
                ball.bounce_y()
                self._audio_service.play_sound(bounce_sound)

        else:
            callback.on_next(GAME_OVER)
