from constants import *
from game.casting.actor import Actor


class Scores(Actor):
    """The game scores."""

    def __init__(self, debug = False):
        """Constructs a score.

        Args:Args:
          
            debug: If it is being debugged.
        """
        super().__init__(debug)
        self._player_scores = [0,0]
   
    def add_score(self,player=1):
        """ Adds one point to a player
        Args:

        Player(int) = player to add score(1 or 2)
         """
        if (self._player_scores[0]<MAXIMUM_SCORE) and (self._player_scores[1]<MAXIMUM_SCORE):
            self._player_scores[player - 1] += 1

    def get_score(self, player = 1):
        """ Get the score of a player 

        Returns:
        A number representing the score of the specified player.
        """
        return self._player_scores[player -  1]

    def reset(self):
        """ Resets the scores back to their defauly values"""

        self._player_scores = [0,0]