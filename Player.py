# =======================================================================
#                           General Documentation

"""Module that contains player class
"""

# ---------------- Module General Import and Declarations ---------------

import numpy as np


# -------------------- Class: Player ------------------------------------
class Player(object):
    """Create and manage Player variables and attributes
    
        Variables:
            skill: Temp variable to quantify skill of player
            mmr: Current MMR of player
            rankUpMatch: if the player is on a match that would rank them up
            rankDownMatch: if the player is on a match that would rank them down
            has_played: if the player has already played a game
            amountOfGamesPlayed: the number of matches the player has played
            lp: The amount of lp a player currently has
            is_online: Checks if the player is online and playing
            rank: The rank of the player
            rankDivision: The division of the players rank
    """

    def __init__(self, mmr_default=1500):
        self.mmr = mmr_default
        self.rank = 9
        self.rankDivision = 1
        self.lp = 0
        self.amountOfGamesPlayed = 0
        self.rankUpMatch = False
        self.rankDownMatch = False
        self.has_played = False
        self.userCreated = False

        #  Skill Variables
        self.communication = np.random.normal(5, 2)
        self.tilt = np.random.normal(5, 3)
        self.internet = 8 - np.random.normal(2, 1)
        self.leadership = np.random.normal(5, 3)
        self.gameKnowledge = np.random.normal(5, 3)
        self.reactionTimes = np.random.normal(5, 3)
        self.early_game = np.random.normal(5, 3)
        self.late_game = np.random.normal(5, 3)
        self.mechanics = np.random.normal(5, 3)

        self.is_online = True

    # -------------------- Function: rankUp ------------------------------------

    def rankUp(self):
        """Allows the player to rank up and assigns rank based on mmr
        
            Variables: 
                bucket = to the bucket/rank the player should fall into
        """

        # -If currently unranked

        if (self.amountOfGamesPlayed < 10):
            return

        if (self.rank == 9):

            bucket = int(round(self.mmr / 100))

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
                self.rankUpMatch = False
                return

        # - resets lp and rankUpMatch

        self.rankUpMatch = False
        self.lp = 0

    # -------------------- Function: rankDown ------------------------------------

    def rankDown(self):
        """Moves the player down in ranks
        """

        # -If player is currently unranked

        if (self.amountOfGamesPlayed < 10):
            return

        # -If the player is below master

        if (self.rank < 6):
            if (self.rankDivision == 4 and self.rank == 0):
                self.rank = 0
            elif (self.rankDivision == 4):
                self.rank -= 1
                self.rankDivision = 1
            else:
                self.rankDivision += 1

        # -If the player is master or better

        else:
            self.rank -= 1
            self.rankDivision = 1

        # - Resets the rankDownMatch and places the player with 30 lp

        self.rankDownMatch = False
        self.lp = 30

    # -------------------- Function: createUserPlayer ------------------------------------

    def createUserPlayer(self, communication, tilt, internet, leadership,
                         gameKnowledge, reactionTimes, early_game, late_game,
                         mechanics):
        """Allows players to create their own player and enter in their skill levels
            
            Variables: Line up with player variables for the init
        """

        self.userCreated = True
        self.communication = communication
        self.tilt = tilt
        self.internet = internet
        self.leadership = leadership
        self.gameKnowledge = gameKnowledge
        self.reactionTimes = reactionTimes
        self.early_game = early_game
        self.late_game = late_game
        self.mechanics = mechanics


    # -------------------- Function: _test_rank_methods ------------------------

    def _test_rank_min_max(self):
        """
        Testing ranking methods in test suite
        :return: rank after rankUp, division after rankUp,
                 rank after rankDown, division after rankDown
        """

        # -Starts at lowest rank

        self.amountOfGamesPlayed = 20
        self.rank = 0
        self.rankDivision = 4

        # -Ranks all the way up

        for i in range(26):
            self.rankUp()
        rank_up = self.rank
        division_up = self.rankDivision

        # -Ranks all the way down

        for i in range(26):
            self.rankDown()
        rank_down = self.rank
        division_down = self.rankDivision
        return rank_up, division_up, rank_down, division_down


    # -------------------- Function: _test_placements ------------------------
    
    def _test_placements(self, mmr):
        """
        Testing placement portion of rankUp
        :param mmr: mmr for bucket test
        :return: rank and division
        """

        self.amountOfGamesPlayed = 10
        self.mmr = mmr
        self.rank = 9
        self.rankUp()
        return self.rank, self.rankDivision
