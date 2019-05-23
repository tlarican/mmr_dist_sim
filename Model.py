import numpy as np

from Player import Player
from Graphing import showRanksUnsorted


class Model(object):
    def __init__(self, number_players=1000):
        self.player_list = []
        for i in range(number_players):
            self.player_list.append(Player())
        showRanksUnsorted(self.player_list)
        self.rank_mins = []
        

    def _test_player_list_size(self):
        return len(self.player_list)

#- Made this to test the graphing method

bob = Model()
