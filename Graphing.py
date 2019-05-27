# =======================================================================
#                           General Documentation

"""Multi Function module to show figures and graphs of data.

    see function docstring for description
"""

# ---------------- Module General Import and Declarations ---------------

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#  TODO(Conor): Running test suite results in color graph showing black and white
# -------------------- General Function:showRanks ---------------------

def showRanksUnsorted(players):
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
            ax: axis used to plot graph
            size: allows me to create ranks
            r: used to track rows
            c: used to track columns
            img: used to show image of the cells
        
        Output: Returns graphRanks and also shows it.
    """

    # - Makes sure there is enough cells to show all players
    # - by increasing the amount of rows and columns

    rows = 10
    columns = 10

    while ((rows * columns) < np.size(players)):
        rows = rows + 2
        columns = columns + 2

    # - Variable Declarations

    r = 0
    c = 0
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_axes((0.0, 0.0, 1, 1), frameon=False)
    size = np.size(players)
    Ranks = np.ones((size, 2))
    graphRanks = np.zeros((rows, columns, 3), dtype='f')

    # - Runs through players inserting the rank and division
    # - into the Ranks array

    for i in range(size):
        for j in range(2):
            if (j == 0):
                Ranks[i, j] = players[i].rank
            else:
                Ranks[i, j] = players[i].rankDivision

    # - Runs through the Ranks array setting the colors of the cells
    # - Based on the values given

    for i in range(size):

        # - moves to next spot in graphRanks if needed
        if (c >= columns):
            c = 0
            r = r + 1

        # - Iron Ranks

        if (Ranks[i, 0] == 0 and Ranks[i, 1] == 4):
            graphRanks[r, c, :] = (.2, .2, .2)
            c = c + 1
        elif (Ranks[i, 0] == 0 and Ranks[i, 1] == 3):
            graphRanks[r, c, :] = (.3, .3, .3)
            c = c + 1
        elif (Ranks[i, 0] == 0 and Ranks[i, 1] == 2):
            graphRanks[r, c, :] = (.4, .4, .4)
            c = c + 1
        elif (Ranks[i, 0] == 0 and Ranks[i, 1] == 1):
            graphRanks[r, c, :] = (.5, .5, .5)
            c = c + 1


        # - Bronze Ranks

        elif (Ranks[i, 0] == 1 and Ranks[i, 1] == 4):
            graphRanks[r, c, :] = (.79, .39, .0)
            c = c + 1
        elif (Ranks[i, 0] == 1 and Ranks[i, 1] == 3):
            graphRanks[r, c, :] = (.99, .5, .0)
            c = c + 1
        elif (Ranks[i, 0] == 1 and Ranks[i, 1] == 2):
            graphRanks[r, c, :] = (.99, .6, .19)
            c = c + 1
        elif (Ranks[i, 0] == 1 and Ranks[i, 1] == 1):
            graphRanks[r, c, :] = (.99, .69, .38)
            c = c + 1


        # - Silver Ranks

        elif (Ranks[i, 0] == 2 and Ranks[i, 1] == 4):
            graphRanks[r, c, :] = (.6, .6, .6)
            c = c + 1
        elif (Ranks[i, 0] == 2 and Ranks[i, 1] == 3):
            graphRanks[r, c, :] = (.7, .7, .7)
            c = c + 1
        elif (Ranks[i, 0] == 2 and Ranks[i, 1] == 2):
            graphRanks[r, c, :] = (.8, .8, .8)
            c = c + 1
        elif (Ranks[i, 0] == 2 and Ranks[i, 1] == 1):
            graphRanks[r, c, :] = (.88, .88, .88)
            c = c + 1


        # - Gold Ranks

        elif (Ranks[i, 0] == 3 and Ranks[i, 1] == 4):
            graphRanks[r, c, :] = (.72, .64, .04)
            c = c + 1
        elif (Ranks[i, 0] == 3 and Ranks[i, 1] == 3):
            graphRanks[r, c, :] = (.85, .64, .13)
            c = c + 1
        elif (Ranks[i, 0] == 3 and Ranks[i, 1] == 2):
            graphRanks[r, c, :] = (.9, .7, .04)
            c = c + 1
        elif (Ranks[i, 0] == 3 and Ranks[i, 1] == 1):
            graphRanks[r, c, :] = (.99, .84, .0)
            c = c + 1


        # - Platinum ranks

        elif (Ranks[i, 0] == 4 and Ranks[i, 1] == 4):
            graphRanks[r, c, :] = (.18, .31, .31)
            c = c + 1
        elif (Ranks[i, 0] == 4 and Ranks[i, 1] == 3):
            graphRanks[r, c, :] = (.0, .5, .5)
            c = c + 1
        elif (Ranks[i, 0] == 4 and Ranks[i, 1] == 2):
            graphRanks[r, c, :] = (.0, .6, .6)
            c = c + 1
        elif (Ranks[i, 0] == 4 and Ranks[i, 1] == 1):
            graphRanks[r, c, :] = (.13, .695, .66)
            c = c + 1


        # - Diamond ranks

        elif (Ranks[i, 0] == 5 and Ranks[i, 1] == 4):
            graphRanks[r, c, :] = (.25, .25, .44)
            c = c + 1
        elif (Ranks[i, 0] == 5 and Ranks[i, 1] == 3):
            graphRanks[r, c, :] = (.0, .0, .55)
            c = c + 1
        elif (Ranks[i, 0] == 5 and Ranks[i, 1] == 2):
            graphRanks[r, c, :] = (.0, .0, .8)
            c = c + 1
        elif (Ranks[i, 0] == 5 and Ranks[i, 1] == 1):
            graphRanks[r, c, :] = (.0, .0, .99)
            c = c + 1

            # - Master Rank

        elif (Ranks[i, 0] == 6):
            graphRanks[r, c, :] = (.5, .0, .5)
            c = c + 1


        # - GrandMaster Rank

        elif (Ranks[i, 0] == 7):
            graphRanks[r, c, :] = (.58, .0, .82)
            c = c + 1


        # - Challenger Rank

        elif (Ranks[i, 0] == 8):
            graphRanks[r, c, :] = (.99, .0, .0)
            c = c + 1


        # - Unranked

        else:
            graphRanks[r, c, :] = (0, 0, 0)
            c = c + 1

    # - Runs through remaining cells seeting them to white
    # - for empty

    while (r < rows):
        while (c < columns):
            graphRanks[r, c, :] = (.99, .99, .99)
            c = c + 1
        c = 0
        r = r + 1

    img = ax.imshow(graphRanks, interpolation='none',
                    extent=[0, rows, 0, columns],
                    aspect="auto",
                    zorder=0)

    plt.show()

    # - End of showRanksUnsorted function


def showMMR(players):
    """This will provide a histogram of the players 
        mmr distribution. It will also provide a graph of 
        points and a line of best fit using the players mmr
        and skill
        
        Variables:
            players: list of player objects
            mmr: an array of player mmr
            skill: an array of player skill
            size: The size of the players list
            
        Output: Prints the histogram and graph of data 
    """

    # -Variable declarations

    size = np.size(players)
    mmr = np.zeros(size)
    skill = np.zeros(size)

    # - Sets the data in the arrays for mmr and skill

    for i in range(size):
        mmr[i] = players[i].mmr
        skill[i] = players[i].skill

    # -Plots the histogram

    plt.figure(1)
    plt.title("Distribution of players by MMR")
    plt.hist(mmr, bins=10)
    plt.xlabel("MMR")
    plt.ylabel("Frequency")

    # - Graphs the scatter plot and line of best fit

    plt.figure(2)
    plt.scatter(skill, mmr)

    # - Borrowed from https://stackoverflow.com/questions/22239691/code-for-best-fit-straight-line-of-a-scatter-plot-in-python
    plt.plot(np.unique(skill), np.poly1d(np.polyfit(skill, mmr, 1))(np.unique(skill)), "r-")

    plt.title("Skill vs. MMR")
    plt.axis([-2, 10, 0, 2000])
    plt.xlabel("Skill")
    plt.ylabel("MMR")

    # -Shows the plots

    plt.show()
