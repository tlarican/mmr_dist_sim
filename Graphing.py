# =======================================================================
#                           General Documentation

"""Multi Function module to show figures and graphs of data.
"""

# ---------------- Module General Import and Declarations ---------------

import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# -------------------- General Function:showPlayerStats ---------------------

def showPlayerStats(players):
    """This will look for the player the user created and get the stats
    
        Variables:
            players: a list of the players 
            count: To track where you're looking for the player
    """

    # -Variable Declarations

    count = 0
    

    # -Prints the stats

    print("Amount of games played:", players[count].amountOfGamesPlayed)
    print("Rank:", players[count].rank, "Rank Division:", players[count].rankDivision, \
          "Lp:", players[count].lp)
    print("MMR:", players[count].mmr)


# -------------------- General Function:showRanks ---------------------

def showRanksUnsorted(players):
    """This will show a figure of the players ranks
        unsorted. Each cell will show a color representing 
        the rank that the player is.
            
        Variables:
            Players: A numpy array of player objects
            rows: The amount of rows you want
            columns: The amount of columns you want
            ranksGraphArray: A numpy array of the player ranks
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
        rows = rows + 5
        columns = columns + 5

    # - Variable Declarations

    r = 0
    c = 0
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_axes((0.0, 0.0, 1, 1), frameon=False)
    size = np.size(players)
    rankGraphArray = np.zeros(size)
    graphRanks = np.zeros((rows, columns, 3), dtype='f')

    # - Runs through players inserting the rank and division
    # - into the rankGraphArray

    for i in range(size):
        if (players[i].rank == 0 and players[i].rankDivision == 4):
            rankGraphArray[i] = 0
        elif (players[i].rank == 0 and players[i].rankDivision == 3):
            rankGraphArray[i] = 1
        elif (players[i].rank == 0 and players[i].rankDivision == 2):
            rankGraphArray[i] = 2
        elif (players[i].rank == 0 and players[i].rankDivision == 1):
            rankGraphArray[i] = 3
        elif (players[i].rank == 1 and players[i].rankDivision == 4):
            rankGraphArray[i] = 4
        elif (players[i].rank == 1 and players[i].rankDivision == 3):
            rankGraphArray[i] = 5
        elif (players[i].rank == 1 and players[i].rankDivision == 2):
            rankGraphArray[i] = 6
        elif (players[i].rank == 1 and players[i].rankDivision == 1):
            rankGraphArray[i] = 7
        elif (players[i].rank == 2 and players[i].rankDivision == 4):
            rankGraphArray[i] = 8
        elif (players[i].rank == 2 and players[i].rankDivision == 3):
            rankGraphArray[i] = 9
        elif (players[i].rank == 2 and players[i].rankDivision == 2):
            rankGraphArray[i] = 10
        elif (players[i].rank == 2 and players[i].rankDivision == 1):
            rankGraphArray[i] = 11
        elif (players[i].rank == 3 and players[i].rankDivision == 4):
            rankGraphArray[i] = 12
        elif (players[i].rank == 3 and players[i].rankDivision == 3):
            rankGraphArray[i] = 13
        elif (players[i].rank == 3 and players[i].rankDivision == 2):
            rankGraphArray[i] = 14
        elif (players[i].rank == 3 and players[i].rankDivision == 1):
            rankGraphArray[i] = 15
        elif (players[i].rank == 4 and players[i].rankDivision == 4):
            rankGraphArray[i] = 16
        elif (players[i].rank == 4 and players[i].rankDivision == 3):
            rankGraphArray[i] = 17
        elif (players[i].rank == 4 and players[i].rankDivision == 2):
            rankGraphArray[i] = 18
        elif (players[i].rank == 4 and players[i].rankDivision == 1):
            rankGraphArray[i] = 19
        elif (players[i].rank == 5 and players[i].rankDivision == 4):
            rankGraphArray[i] = 20
        elif (players[i].rank == 5 and players[i].rankDivision == 3):
            rankGraphArray[i] = 21
        elif (players[i].rank == 5 and players[i].rankDivision == 2):
            rankGraphArray[i] = 22
        elif (players[i].rank == 5 and players[i].rankDivision == 1):
            rankGraphArray[i] = 23
        elif (players[i].rank == 6):
            rankGraphArray[i] = 24
        elif (players[i].rank == 7):
            rankGraphArray[i] = 25
        elif (players[i].rank == 8):
            rankGraphArray[i] = 26
        else:
            rankGraphArray[i] = 27

    rankGraphArray.sort()

    # - Runs through the ranksGrapharray setting the colors of the cells
    # - Based on the values given

    for i in range(size):

        # - moves to next spot in graphRanks if needed
        if (c >= columns):
            c = 0
            r = r + 1

        # - Iron Ranks

        if (rankGraphArray[i] == 0):
            graphRanks[r, c, :] = (.2, .2, .2)
            c = c + 1
        elif (rankGraphArray[i] == 1):
            graphRanks[r, c, :] = (.3, .3, .3)
            c = c + 1
        elif (rankGraphArray[i] == 2):
            graphRanks[r, c, :] = (.4, .4, .4)
            c = c + 1
        elif (rankGraphArray[i] == 3):
            graphRanks[r, c, :] = (.5, .5, .5)
            c = c + 1


        # - Bronze Ranks

        elif (rankGraphArray[i] == 4):
            graphRanks[r, c, :] = (.79, .39, .0)
            c = c + 1
        elif (rankGraphArray[i] == 5):
            graphRanks[r, c, :] = (.99, .5, .0)
            c = c + 1
        elif (rankGraphArray[i] == 6):
            graphRanks[r, c, :] = (.99, .6, .19)
            c = c + 1
        elif (rankGraphArray[i] == 7):
            graphRanks[r, c, :] = (.99, .69, .38)
            c = c + 1


        # - Silver Ranks

        elif (rankGraphArray[i] == 8):
            graphRanks[r, c, :] = (.6, .6, .6)
            c = c + 1
        elif (rankGraphArray[i] == 9):
            graphRanks[r, c, :] = (.7, .7, .7)
            c = c + 1
        elif (rankGraphArray[i] == 10):
            graphRanks[r, c, :] = (.8, .8, .8)
            c = c + 1
        elif (rankGraphArray[i] == 11):
            graphRanks[r, c, :] = (.88, .88, .88)
            c = c + 1


        # - Gold Ranks

        elif (rankGraphArray[i] == 12):
            graphRanks[r, c, :] = (.72, .64, .04)
            c = c + 1
        elif (rankGraphArray[i] == 13):
            graphRanks[r, c, :] = (.85, .64, .13)
            c = c + 1
        elif (rankGraphArray[i] == 14):
            graphRanks[r, c, :] = (.9, .7, .04)
            c = c + 1
        elif (rankGraphArray[i] == 15):
            graphRanks[r, c, :] = (.99, .84, .0)
            c = c + 1


        # - Platinum ranks

        elif (rankGraphArray[i] == 16):
            graphRanks[r, c, :] = (.18, .31, .31)
            c = c + 1
        elif (rankGraphArray[i] == 17):
            graphRanks[r, c, :] = (.0, .5, .5)
            c = c + 1
        elif (rankGraphArray[i] == 18):
            graphRanks[r, c, :] = (.0, .6, .6)
            c = c + 1
        elif (rankGraphArray[i] == 19):
            graphRanks[r, c, :] = (.13, .695, .66)
            c = c + 1


        # - Diamond ranks

        elif (rankGraphArray[i] == 20):
            graphRanks[r, c, :] = (.0, .0, .40)
            c = c + 1
        elif (rankGraphArray[i] == 21):
            graphRanks[r, c, :] = (.0, .0, .55)
            c = c + 1
        elif (rankGraphArray[i] == 22):
            graphRanks[r, c, :] = (.0, .0, .8)
            c = c + 1
        elif (rankGraphArray[i] == 23):
            graphRanks[r, c, :] = (.0, .0, .99)
            c = c + 1

            # - Master Rank

        elif (rankGraphArray[i] == 24):
            graphRanks[r, c, :] = (.5, .0, .5)
            c = c + 1


        # - GrandMaster Rank

        elif (rankGraphArray[i] == 25):
            graphRanks[r, c, :] = (.58, .0, .82)
            c = c + 1


        # - Challenger Rank

        elif (rankGraphArray[i] == 26):
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
    ranks = np.zeros(size)
    
    
    # - Sets the data in the arrays for mmr and skill

    for i in range(size):
        mmr[i] = players[i].mmr
        skill[i] = players[i].communication + players[i].tilt + \
                   players[i].internet + players[i].leadership + \
                   players[i].gameKnowledge + players[i].reactionTimes + \
                   players[i].early_game + players[i].late_game + \
                   players[i].mechanics
        ranks[i] = players[i].rank


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

    plt.title("Aggregate Skill vs. MMR")
    plt.axis([10, 80, 0, 2800])
    plt.xlabel("Skill")
    plt.ylabel("MMR")


    # -Plots histogram for skill and rank

    plt.figure(3)
    plt.title("Skill distribution")
    plt.hist(skill)
    plt.xlabel("Skill")
    plt.ylabel("Frequency")

    plt.figure(4)
    plt.hist(ranks, 9)
    plt.title("Rank distrubution")
    plt.xlabel("rank")
    plt.ylabel("frequency")


    # -Shows the plots

    plt.show()
