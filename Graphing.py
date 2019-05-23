#=======================================================================
#                           General Documentation

"""Multi Function module to show figures and graphs of data.

    see function docstring for description
"""

#---------------- Module General Import and Declarations ---------------

import numpy as np
import matplotlib.pyplot as plt

#-------------------- General Function:showRanks ---------------------

def showRanksUnsorted(players, rows, columns):
    """This will show a figure of the players ranks
        unsorted. Each cell will show a color representing 
        the rank that the player is.
            
        Variables:
            Players: A numpy array of player objects
            rows: The amount of rows you want
            columns: The amount of columns you want
            Ranks: A numpy array of the player ranks
            graphRanks: A numpy array using rgb to color
                code the cells
            fig: The figure window that will be shown
            ax: used to plot graph
            r: used to track rows
            c: used to track columns
        
        Output: Returns graphRanks and also shows it.
    """
    
    #- Makes sure there is enough cells to show all players
    #- by increasing the amount of rows and columns
    
    while((rows*columns) < np.size(players)):
        rows = rows + 2
        columns = columns + 2
    
    
    #- Variable Declarations
    
    r = 0
    c = 0
    fig = plt.figure(figsize=(9.5, 4+(1./8)))
    ax = fig.add_axes( (0.1, 0.1, 0.1, 0.1), frameon=False )
    Ranks = np.zeros(np.size(players), 2)
    graphRanks = np.zeros((rows, columns, 3), dtype='f')
    
    
    #- Runs through players inserting the rank and division
    #- into the Ranks array
    
    for i in range(np.size(players)):
        for j in range(2):
            if(j == 0):
                Ranks[i, j] = players[i].rank
            else:
                Ranks[i, j] = players[i].rankDivision
    
    
    #- Runs through the Ranks array setting the colors of the cells
    #- Based on the values given
    
    for i in range(np.size(players)):
        
        #- moves to next spot in graphRanks if needed
        if(c >= columns):
            c = 0
            r = r + 1
            
            
        #- Iron Ranks
        
        if(Ranks[i, 0] == 0 and Ranks[i, 1] == 4):
            graphRanks[r, c, :] = (.2, .2, .2)
            c = c + 1
        elif(Ranks[i, 0] == 0 and Ranks[i, 1] == 3):
            graphRanks[r, c, :] = (.3, .3, .3)
            c = c + 1
        elif(Ranks[i, 0] == 0 and Ranks[i, 1] == 2):
            graphRanks[r, c, :] = (.4, .4, .4)
            c = c + 1
        elif(Ranks[i, 0] == 0 and Ranks[i, 1] == 1):
            graphRanks[r, c, :] = (.5, .5, .5)
            c = c + 1
            
            
        #- Bronze Ranks
        
        elif(Ranks[i, 0] == 1 and Ranks[i, 1] == 4):
            graphRanks[r, c, :] = (.79, .39, .0)
            c = c + 1
        elif(Ranks[i, 0] == 1 and Ranks[i, 1] == 3):
            graphRanks[r, c, :] = (.99, .5, .0)
            c = c + 1
        elif(Ranks[i, 0] == 1 and Ranks[i, 1] == 2):
            graphRanks[r, c, :] = (.99, .6, .19)
            c = c + 1
        elif(Ranks[i, 0] == 1 and Ranks[i, 1] == 1):
            graphRanks[r, c, :] = (.99, .69, .38)
            c = c + 1
        
        
        #- Silver Ranks
        
        elif(Ranks[i, 0] == 2 and Ranks[i, 1] == 4):
            graphRanks[r, c, :] = (.6, .6, .6)
            c = c + 1
        elif(Ranks[i, 0] == 2 and Ranks[i, 1] == 3):
            graphRanks[r, c, :] = (.7, .7, .7)
            c = c + 1
        elif(Ranks[i, 0] == 2 and Ranks[i, 1] == 2):
            graphRanks[r, c, :] = (.8, .8, .8)
            c = c + 1
        elif(Ranks[i, 0] == 2 and Ranks[i, 1] == 1):
            graphRanks[r, c, :] = (.88, .88, .88)
            c = c + 1
        
                    
            
    
    
    
    
    
    
    
    