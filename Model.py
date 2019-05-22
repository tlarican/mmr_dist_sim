import numpy as np
from Player import Player


class Model(object):
    def __init__(self, number_players=1000):
        self.player_list = []
        for i in range(number_players):
            self.player_list.append(Player())

