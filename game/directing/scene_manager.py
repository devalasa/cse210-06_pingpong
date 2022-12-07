import csv
from constants import *
from game.casting.ball import Ball
from game.casting.body import Body
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.racket import Racket
from game.casting.stats import Stats
from game.casting.text import Text
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.collide_borders_action import CollideBordersAction
from game.scripting.collide_racket_action import CollideRacketAction
from game.scripting.control_racket_action import ControlRacketAction
from game.scripting.draw_ball_action import DrawBallAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_racket_action import DrawRacketAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_ball_action import MoveBallAction
from game.scripting.move_racket_action import MoveRacketAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""

    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)
    COLLIDE_BORDERS_ACTION = CollideBordersAction(
        PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_RACKET_ACTION = CollideRacketAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    CONTROL_RACKET_ACTION = ControlRacketAction(KEYBOARD_SERVICE)
    DRAW_BALL_ACTION = DrawBallAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_RACKET_ACTION = DrawRacketAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(
        AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_BALL_ACTION = MoveBallAction()
    MOVE_RACKET_ACTION = MoveRacketAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == NEXT_SCENE:
            self._prepare_next_level(cast, script)
        elif scene == IN_PLAY:
            self._prepare_try_again(cast, script)
        elif scene == CONTINUE:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:
            self._prepare_game_over(cast, script)

    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------

    def _prepare_new_game(self, cast, script):
        self._add_score_stats(cast)
        self.add_score1(cast)
        self.add_score2(cast)
        self._add_ball(cast)
        self._add_racket(cast)
        self._add_dialog(cast, ENTER_TO_START)
        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(
            self.KEYBOARD_SERVICE, NEXT_SCENE))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)

    def _prepare_next_level(self, cast, script):
        self._add_ball(cast)
        self._add_racket(cast)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(
            self.AUDIO_SERVICE, WELCOME_SOUND))

    def _prepare_try_again(self, cast, script):
        self._add_ball(cast)
        self._add_racket(cast)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):
        self._activate_ball(cast)
        cast.clear_actors(DIALOG_GROUP)
        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_RACKET_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        self._add_ball(cast)
        self._add_racket(cast)
        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------

    def _activate_ball(self, cast):
        ball = cast.get_first_actor(BALL_GROUP)
        ball.release()

    def _add_ball(self, cast):
        cast.clear_actors(BALL_GROUP)
        size = Point(BALL_WIDTH, BALL_HEIGHT)
        velocity = Point(0, 0)
        y = CENTER_Y - BALL_HEIGHT
        x = CENTER_X - BALL_WIDTH
        position = Point(x, y)
        body = Body(position, size, velocity)
        image = Image(BALL_IMAGE)
        ball = Ball(body, image, True)
        cast.add_actor(BALL_GROUP, ball)

    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SIZE, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def add_score1(self, cast):
        cast.clear_actors(SCORE_1_GROUP)
        text = Text(PLAYER_1_SCORE_FORMAT, FONT_FILE, FONT_SIZE, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_1_GROUP, label)

    def add_score2(self, cast):
        cast.clear_actors(SCORE_2_GROUP)
        text = Text(PLAYER_2_SCORE_FORMAT, FONT_FILE, FONT_SIZE, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_2_GROUP, label)

    def _add_score_stats(self, cast):
        cast.clear_actors(SCORE_STATS_GROUP)
        score_stats = Stats()
        cast.add_actor(SCORE_STATS_GROUP, score_stats)

    def _add_racket(self, cast):
        cast.clear_actors(RACKET_GROUP)
        x = SCREEN_WIDTH - RACKET_HEIGHT
        y = CENTER_Y - RACKET_WIDTH / 2
        size = Point(RACKET_WIDTH, RACKET_HEIGHT)
        velocity = Point(0, 0)
        y = CENTER_Y

        # PLAYER 1
        image1 = Image(RACKET_IMAGE, 1, 90)
        x1 = 40
        position1 = Point(x1, y)
        body1 = Body(position1, size, velocity)
        paddle1 = Racket(body1, image1, True)

        # PLAYER 2
        image2 = Image(RACKET_IMAGE, 1, 90)
        x2 = SCREEN_WIDTH - 20
        position2 = Point(x2, y)
        body2 = Body(position2, size, velocity)
        paddle2 = Racket(body2, image2, True)

        cast.add_actor(RACKET_GROUP, paddle1)
        cast.add_actor(RACKET_GROUP, paddle2)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)

    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_BALL_ACTION)
        script.add_action(OUTPUT, self.DRAW_RACKET_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)

    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)

    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_BALL_ACTION)
        script.add_action(UPDATE, self.MOVE_RACKET_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_RACKET_ACTION)
        script.add_action(UPDATE, self.MOVE_RACKET_ACTION)
