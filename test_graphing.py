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
    
    # -------------------- Function: test_show_player_stats ------------------------------------
    
    def test_show_player_stats(self):
        """Tests the showPlayerStats function in graphing
        """
        
        #-Creates a list and gives one player
        
        player = []
        player.append(Player())
        
        #-Shows the player stats
        
        Graphing.showPlayerStats(player)
        
    
    # -------------------- Function: test_show_ranks_unsorted ------------------------------------
    
    def test_show_ranks_unsorted(self):
        """Tests showRanksUnsorted by creating a list
            of players showing each rank and division
            
            Variables:
                players = a list of player objects
                rank = used to give a rank to the players
                division = used to give a division to the players
        """
        
        #- Variable declarations
        
        players = []
        rank = 0
        division = 4
        
        
        #- Creates 27 players
        
        for i in range(27):
            players.append(Player())
            
        
        #- Gives ranks and divisions to the 27 players
        
        for i in range(27):
            
            #- If the division is 0 it should go up a rank
            
            if(division == 0):
                division = 4
                rank += 1
                
            #- If its at rank 6 or 7 it should set division to 1
            
            if(rank == 6 or rank == 7):
                division = 1
                
            #- Sets the amountOfGamesPlayed, ranks, and division for the players
            #- Moves division down one
            
            players[i].amountOfGamesPlayed = 11
            players[i].rank = rank
            players[i].rankDivision = division
            division -= 1
        
        #-Runs graphing method with the players
        
        Graphing.showRanksUnsorted(players)
     
     
    # -------------------- Function: test_show_mmr ------------------------------------ 
      
    def test_show_mmr(self):
        """Creates a list of players and tests showMMR
        
            Variables:
                players: list of player objects
        """
        
        #- Creates a list of players
        
        players = []
        for i in range(27):
            players.append(Player())
            
        
        #- Uses showMMR with the player list
        
        Graphing.showMMR(players)    
        
        