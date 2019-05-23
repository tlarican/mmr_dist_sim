#=======================================================================
#                           General Documentation

"""Multi Function module to show figures and graphs of data.

    see function docstring for description
"""

#---------------- Module General Import and Declarations ---------------

import numpy as np
import matplotlib.pyplot as plt

#-------------------- General Function:showRanks ---------------------

def showRanksUnsorted(players, m, n):
    """This will show a figure of the players ranks
        unsorted. Each cell will show a color representing 
        the rank that the player is.
            
        Variables:
            Players: A numpy array of player objects
            m: The amount of rows you want
            n: The amount of columns you want
            Ranks: A numpy array of the player ranks
            graphRanks: A numpy array using rgb to color
                code the cells
        
        Output: Returns graphRanks and also shows it.
    """
    
    Ranks = np.zeros(np.size(players), 2)
    
    for i in range(np.size(players)):
        Ranks[i] = players[i].rank
        
    
    
    
    
    
    
    
    