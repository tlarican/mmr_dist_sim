# =======================================================================
#                           General Documentation

"""Module that contains player class

    see function docstring for description
"""

# ---------------- Module General Import and Declarations ---------------

import numpy as np


# -------------------- Class: Player ------------------------------------

class Player(object):
    """Create and manage Player variables and attributes
    
        Variables:
            skill: Temp variable to quantify skill of player
            mmr: Current MMR of player
    """

    def __init__(self, mmr_default=1500):
        """
            Random thoughts on variables we could use
        
            self.lastHiting = np.random.randint(1, 11)
            self.tilt = np.random.randint(1, 11)
            self.mechanics = np.random.randint(1, 11)
            self.teamFighting = np.random.randint(1, 11)
            self.waveManagement = np.random.randint(1, 11)
        """
        self.skill = np.random.normal(5, 2)
        self.mmr = mmr_default
        self.rankUpMatch = False
        self.rankDownMatch = False
        self.has_played = False
        self.amountOfGamesPlayed = 0
        self.lp = 0
        self.is_online = True
        self.rank = 9
        self.rankDivision = 1
        

    # -------------------- Function: rankUp ------------------------------------

    def rankUp(self):
        """Allows the player to rank up and assigns rank based on mmr
        
            Variables: 
                bucket = to the bucket/rank the player should fall into
        """

        # -If currently unranked
        if(self.amountOfGamesPlayed < 10):
            return
            
        if (self.rank == 9):

            bucket = round(self.mmr / 100)

            # -Finds the rank based off bucket and places it.

            if (bucket == 1):
                self.rank = 0
                self.rankDivision = 4
            elif (bucket == 2):
                self.rank = 0
                self.rankDivision = 3
            elif (bucket == 3):
                self.rank = 0
                self.rankDivision = 2
            elif (bucket == 4):
                self.rank = 0
                self.rankDivision = 1
            elif (bucket == 5):
                self.rank = 1
                self.rankDivision = 4
            elif (bucket == 6):
                self.rank = 1
                self.rankDivision = 3
            elif (bucket == 7):
                self.rank = 1
                self.rankDivision = 2
            elif (bucket == 8):
                self.rank = 1
                self.rankDivision = 1
            elif (bucket == 9):
                self.rank = 2
                self.rankDivision = 4
            elif (bucket == 10):
                self.rank = 2
                self.rankDivision = 3
            elif (bucket == 11):
                self.rank = 2
                self.rankDivision = 2
            elif (bucket == 12):
                self.rank = 2
                self.rankDivision = 1
            elif (bucket == 13):
                self.rank = 3
                self.rankDivision = 4
            elif (bucket == 14):
                self.rank = 3
                self.rankDivision = 3
            elif (bucket == 15):
                self.rank = 3
                self.rankDivision = 2
            elif (bucket == 16):
                self.rank = 3
                self.rankDivision = 1
            elif (bucket == 17):
                self.rank = 4
                self.rankDivision = 4
            elif (bucket == 18):
                self.rank = 4
                self.rankDivision = 3
            elif (bucket == 19):
                self.rank = 4
                self.rankDivision = 2
            elif (bucket == 20):
                self.rank = 4
                self.rankDivision = 1
            elif (bucket == 21):
                self.rank = 5
                self.rankDivision = 4
            elif (bucket == 22):
                self.rank = 5
                self.rankDivision = 3
            elif (bucket == 23):
                self.rank = 5
                self.rankDivision = 2
            elif (bucket == 24):
                self.rank = 5
                self.rankDivision = 1
            elif (bucket == 25):
                self.rank = 6
                self.rankDivision = 1
            elif (bucket == 26):
                self.rank = 7
                self.rankDivision = 1
            else:
                self.rank = 8
                self.rankDivision = 1


        # -If currently ranked

        else:

            # -If below master

            if (self.rank < 6):
                if (self.rankDivision == 1):
                    self.rank += 1
                    self.rankDivision = 4
                else:
                    self.rankDivision -= 1

            # - If below challenger

            elif (self.rank < 8):
                self.rank += 1
                self.rankDivision = 1

            # - If Challenger

            else:
                self.rank = 8

        self.rankUpMatch = False
        self.lp = 0

    # -------------------- Function: rankDown ------------------------------------

    def rankDown(self):
        """Moves the player down in ranks
        """
        if(self.amountOfGamesPlayed < 10):
            return
            
        if (self.rank < 6):
            if (self.rankDivision == 4 and self.rank == 0):
                self.rank = 0
            elif (self.rankDivision == 4):
                self.rank -= 1
                self.rankDivision = 1
            else:
                self.rankDivision += 1
        else:
            self.rank -= 1
            self.rankDivision = 1

        self.rankDownMatch = False
        self.lp = 50

    # -------------------- Function: _test_rank_methods ------------------------

    def _test_rank_methods(self):
        """
        Testing ranking methods in test suite
        :return: rank after rankUp, divison after rankUp,
                 rank after rankDown, divison after rankDown
        """
        self.amountOfGamesPlayed = 20
        self.rank = 0
        self.rankDivision = 4
        for i in range(26):
            self.rankUp()
        rank_up = self.rank
        division_up = self.rankDivision
        for i in range(26):
            self.rankDown()
        rank_down = self.rank
        division_down = self.rankDivision
        return rank_up, division_up, rank_down, division_down
