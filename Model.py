# =======================================================================
#                           General Documentation

"""Module that contains the Model class

    see function docstring for description
"""

# ---------------- Module General Import and Declarations ---------------

import numpy as np
from Player import Player
import Graphing


# -------------------- Class: Model ------------------------------------

class Model(object):
    def __init__(self, number_players=1000):
        self.player_list = []
        for i in range(number_players):
            self.player_list.append(Player())
        # Graphing.showRanksUnsorted(self.player_list)
        # Graphing.showMMR(self.player_list)
        self.rank_mins = []

    def _test_player_list_size(self):
        return len(self.player_list)

