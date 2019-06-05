# =============================server.py================================
# General Documentation

""" Module that contains functions that deal with matches between
    players created in module

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
#---------------------------- Global Variables ---------------------------
"""
Global Variabls:
    * TEAM_SIZE = 5
"""
#
#
# ---------------------------------- Function: match ----------------------------------------
def match(players):
"""
Method Arguments:
    * players: a 10-element array that contains the 10 players in a 
        match. The first 5 are on one team and the last 5 are on the other.
        
Return:
    * returns 1 if team 1 wins, otherwise 2
    
Variables:
    * team_1_skill_agg: Team 1 average skill
    * team_2_skill_agg: Team 2 average skill
    
    * winner: winner of the match between the two teams.
Return: winner
"""

# ----------------------------- Function: handleMatchResults -------------------------------
def handleMatchResults(players, winner, average_mmr):
"""
Takes the results of a match and adjust player mmr, lp, and rank
    
Method Arguments:
    * players = List of players in match
    * winner = Indicates which team won, 2 for team 1, 1 for team 2
    * average_mmr = The average mmr of the match
"""

# --------------------------------- Function: checkMatch -----------------------------------
def checkMatch(player, gamePosition, lpChange):
"""
Changes the lp and handles ranking up and down for the player
    
Method Arguments:
    * player = the player to change.
    * gamePosition = whether they won or loss.
    * lpChange = the amount of lp that should be changed.
"""

# -------------------------------- Function: pick_lobby -----------------------------------
def pick_lobby(all_players):
"""
Gets matches for as many players as possible
Method Arguments:
    * all_players: np array containing all the players in the simulation.

Variables:
    * online_players: puts all players that are online in a list.
    * ONLINE_COUNT: the amount of players online.
    * match_1_average_mmr: the average mmr for team 1.
    * match_2_average_mmr: the average mmr for team 2.
    * match_average_mmr: the match's average mmr
    * teamOne: One of the team of 5 competitors in a match.
    * teamTwo: Another one of the team of 5 competitors in a match.
    * teamThree: The top ten players.
    * match_result: The winner result of a match.
    * match_1_result: The winner result of the first match.
            
Returns: online players
"""

# ---------------------- Function: _test_match_winner_handling ---------------------------
def _test_match_winner_handling():
"""
Creates list of players to test winning and losing.

Variables:
    * player_list: list of players.