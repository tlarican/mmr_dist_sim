# =======================================================================
#                           General Documentation

"""Module that contains the Model class

    see function docstring for description
"""

# ---------------- Module General Import and Declarations ---------------

import numpy as np
from Player import Player
import Graphing
import server


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

    def _test_player_list_size(self):
        """
        Testing if amount of players initialized is correct
        :return: amount of players initialized
        """
        return len(self.player_list)

model = Model()
model.player_list[0].createUserPlayer(5, 5, 5, 5, 5, 5, 5, 1000000)
for i in range(1000):
    server.pick_lobby(model.player_list)
print(model.player_list[0].skill)
Graphing.showPlayerStats(model.player_list)
