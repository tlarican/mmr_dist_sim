# =======================================================================
#                           General Documentation

"""
Tests for Graphing Class
"""

# ---------------- Module General Import and Declarations ---------------

import Graphing
from Player import Player

class Tests(object):
    """
    Testing object for when test.py is ran through main
    """
    
    def test_show_player_stats(self):
        """Tests the showPlayerStats function in graphing
        """
        player = []
        player.append(Player())
        Graphing.showPlayerStats(player)
        
    
    def test_show_ranks_unsorted(self):
        """Tests showRanksUnsorted by creating a list
            of players showing each rank and division
        """
        players = []
        rank = 0
        division = 4
        for i in range(27):
            players.append(Player())
        for i in range(27):
            if(division == 0):
                division = 4
                rank += 1
            if(rank == 6 or rank == 7):
                division = 1
            players[i].amountOfGamesPlayed = 11
            players[i].rank = rank
            players[i].rankDivision = division
            division -= 1
        
        Graphing.showRanksUnsorted(players)
        
    def test_show_mmr(self):
        """Creates a list of players and 
            tests showMMR
        """
        players = []
        for i in range(27):
            players.append(Player())
        Graphing.showMMR(players)    
        
        