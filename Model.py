# =======================================================================
#                           General Documentation

"""Module that contains the Model class
"""

# ---------------- Module General Import and Declarations ---------------

import numpy as np
from Player import Player
import Graphing
import server
import csv


# -------------------- Class: Model ------------------------------------

class Model(object):
    """
    Mainly holds the players to run matches on.
    """
    
    def __init__(self, number_players=1000):
        """
        Create list of player objects
        :param number_players: Number of players in simulation
        """
        self.player_list = []
        for i in range(number_players):
            self.player_list.append(Player())

    
    # -------------------- Function: to_csv ------------------------------------
    
    def to_csv(self):
        """Write out info for analysis
        """
        with open('Players.csv', 'wt', newline='\n') as out:
            fields = ('mmr', 'communication', 'tilt', 'internet', 'leadership',
                      'gameKnowledge', 'reactionTimes', 'early_game',
                      'late_game', 'mechanics')
            writer = csv.writer(out)
            writer.writerow(fields)
            for iplayer in self.player_list:
                row = (iplayer.mmr, iplayer.communication, iplayer.tilt,
                       iplayer.internet, iplayer.leadership,
                       iplayer.gameKnowledge, iplayer.reactionTimes,
                       iplayer.early_game, iplayer.late_game, iplayer.mechanics)
                writer.writerow(row)

    
    # -------------------- Function: _test_player_list_size ------------------------------------
    
    def _test_player_list_size(self):
        """
        Testing if amount of players initialized is correct
        :return: amount of players initialized
        """
        return len(self.player_list)


if __name__ == "__main__":
    GAMES_TO_SIM = 1000
    SHOW_GRAPHS = True
    model = Model()
    for i in range(GAMES_TO_SIM):
        server.pick_lobby(model.player_list)
    if SHOW_GRAPHS:
        Graphing.showMMR(model.player_list)
        Graphing.showRanksUnsorted(model.player_list)
