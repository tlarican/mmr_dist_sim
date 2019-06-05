# =============================Graphing.py================================
# General Documentation

""" Multi Function module to show figures and graphs of data.

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
# ---------------------------- General Function: showPlayerStats -----------------------------
def showPlayerStats(players):
"""
This will look for the player the user created and get the stats
    
Variables:
    * players: a list of the players 
    * count: To track where you're looking for the player
"""

# ------------------------------- General Function:showRanks ---------------------------------
def showRanksUnsorted(players):
"""
This shows a figure of the players ranks unsorted. Each cell will
show a color representing the rank that the player is.
            
Variables:
    * Players: A numpy array of player objects.
    * rows: The amount of rows you want.
    * columns: The amount of columns you want.
    * ranksGraphArray: A numpy array of the player ranks.
    * graphRanks: A numpy array using rgb to color
        code the cells.
    * fig: The figure window that will be shown.
    * ax: axis used to plot graph.
    * size: allows me to create ranks.
    * r: used to track rows.
    * c: used to track columns.
    * img: used to show image of the cells.
        
Return: graphRanks (also shows it).
"""

# ------------------------------- General Function:showMMR ----------------------------------
def showMMR(players):
"""
This will provide a histogram of the players mmr distribution. It
will also provide a graph of points and a line of best fit using 
the players mmr and skill.
        
Variables:
    * players: list of player objects
    * mmr: an array of player mmr
    * skill: an array of player skill
    * size: The size of the players list
        
Return: (Prints) 
    * histogram
    * graph of data
"""