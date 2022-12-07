from constants import *
from game.scripting.action import Action


class DrawHudAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        stats1 = cast.get_first_actor(STATS_GROUP1)
        stats2 = cast.get_first_actor(STATS_GROUP2)
        self._draw_label(cast, SCORE1_GROUP, SCORE1_FORMAT, stats1.get_score())
        self._draw_label(cast, SCORE2_GROUP, SCORE2_FORMAT, stats2.get_score())
        self._draw_label(cast, ROUND_GROUP, ROUND_FORMAT, stats1.get_level())

    def _draw_label(self, cast, group, format_str, data):
        label = cast.get_first_actor(group)
        text = label.get_text()
        text.set_value(format_str.format(data))
        position = label.get_position()
        self._video_service.draw_text(text, position)

      