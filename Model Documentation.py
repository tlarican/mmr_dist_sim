# =============================Model.py================================
# General Documentation

""" Module that contains model class.

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
# --------------------------------------- Class: Model -----------------------------------------------
"""
Mainly holds the players to run matches on.

Variables:
    * number_players: Number of players in simulation
    * self: Instance of the class. Allows access to attributes and methods
        within the Player class.
"""

# ------------------------------------ Function: to_csv ------------------------------------
def to_csv(self):
"""
Write out info for analysis.

Files:
    * Player.csv: prints out a player's mmr, communication, tilt, internet,
        leadership, gameknowledge, reactionTimes, early_game, late_game,
        and mechanics to the file.
"""

# ------------------------- Function: _test_player_list_size ------------------------------
def _test_player_list_size(self):
"""
Testing if amount of players initialized is correct.

Return: amount of players initialized.
Variables:
    * GAMES_TO_SIM: Amount of games that will be simulated.
    * SHOW_GRAPHS: If graphs should be displayed.
    * model: Creates the model.
"""