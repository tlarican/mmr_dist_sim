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
    
    #-Amount of games that will be simulated
    
    GAMES_TO_SIM = 1000
    
    #-If you want graphs displayed
    
    SHOW_GRAPHS = True
    
    #-Creates the model
    
    model = Model()
    
    #-Select the skills you want for your user created player 
    
    model.player_list[0].createUserPlayer(communication = 6, tilt = 6, internet = 6, leadership = 6, \
                         gameKnowledge = 6, reactionTimes = 6, early_game = 6, late_game = 6, \
                         mechanics = 6)
    
    #-Runs the sims
    
    for i in range(GAMES_TO_SIM):
        server.pick_lobby(model.player_list)
        
    #-Graphs the functions
    
    if SHOW_GRAPHS:
        Graphing.showMMR(model.player_list)
        Graphing.showRanksUnsorted(model.player_list)
        Graphing.showPlayerStats(model.player_list)
