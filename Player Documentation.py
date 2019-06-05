# =============================Player.py================================
# General Documentation

""" Module that contains player class.

    See function docstring for description.
"""

# ===================================================================
#					Additional Documentation
#
# Modification History:
# - May 2019: Original by Tyler Larican, Connor Shabro, Antong Chen, and Rayden Smith.
#    University of Washington.
#
# Notes:
# - Written for Python 2.
# - See comments throughout for more information on created functions.
# ===================================================================
#
#
# --------------------------- Module General Import and Declarations -------------------------
# import non-built-in packages and modules required.
#
#
# --------------------------------------- Class: Player -----------------------------------------------
"""
Create and manage Player variables and attributes

Variables:
    * skill: Temp variable to quantify skill of player
    * mmr: Current MMR of player
    * rankUpMatch: if the player is on a match that would rank them up
    * rankDownMatch: if the player is on a match that would rank them down
    * has_played: if the player has already played a game
    * amountOfGamesPlayed: the number of matches the player has played
    * lp: The amount of lp a player currently has
    * is_online: Checks if the player is online and playing
    * rank: The rank of the player
    * rankDivision: The division of the players rank
"""

# -------------------------------------- Function: rankUp ------------------------------------
def rankUp(self):
"""
Allows the player to rank up and assigns rank based on mmr

Variables: 
    bucket = To the bucket/rank the player should fall into
    
Method Arguments:
    * self: Instance of the class. Allows access to attributes and methods
        within the Player class.
"""

# ------------------------------------ Function: rankDown -----------------------------------
def rankDown(self):
"""
Moves the player down in ranks.

Method Arguments:
    * self: Instance of the class. Allows access to attributes and methods
        within the Player class.
"""

# ------------------------------ Function: createUserPlayer --------------------------------
def createUserPlayer(self, communication, tilt, internet, leadership,
                         gameKnowledge, reactionTimes, early_game, late_game,
                         mechanics):
"""
Allows players to create their own player and enter in their skill levels
            
Method Arguments:
    * self: Instance of the class. Allows access to attributes and methods
        within the Player class.
    * communication: a player skill. A measurment of how good the player is
        at communicating in a team.
    * tilt: a player skill. A measurement of how bad the player is at
        remaining a good sportsman attitude.
    * internet: a player skill. A measurement of the player's internet
        connection quality.
    * leadership: a player skill. A measurement of how good a player's
        ability to lead.
    * gameKnowledge: a player skill. A measurment of the player's experience.
    * reactionTimes: a player skill. A measurement of how fast a player
        can react to the changing atmosphere.
    * early_game: The early game variable.
    * late_game: The early game variable.
    * mechanics: The mechanics of the game.
"""

# ---------------------------- Function: _test_rank_methods ------------------------------
def _test_rank_min_max(self):
"""
Testing ranking methods in test suite

Return: 
    rank after rankUp, division after rankUp,rank after rankDown, 
    division after rankDown
    
Method Arguments:
    * self: Instance of the class. Allows access to attributes and methods
        within the Player class.
"""

# ----------------------------- Function: _test_placements ------------------------------
def _test_placements(self, mmr):
"""
Testing placement portion of rankUp

Return: rank and division

Method Arguments:
    * mmr for bucket test
    * self: Instance of the class. Allows access to attributes and methods
        within the Player class.
"""