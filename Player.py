import numpy as np

#  TODO(Tyler): Create Player Tests
class Player(object):
    """Create and manage Player variables and attributes
    
        Variables:
            skill: Temp variable to quantify skill of player
            mmr: Current MMR of player
    """

    def __init__(self, mmr_default=1400):
        self.skill = np.random.normal(5, 2)
        self.mmr = mmr_default
        self.has_played = False
        #  TODO(Antong): Make this variable a random number based on what you believe the distribution should be
        self.is_online = True
        #  TODO(Tyler): Make this based off the buckets that will be defined in the Model Object
        self.rank = None
        #- Connor - For this rank can you use ints? (0 = iron, 1 = bronze, 2 = silver, 3 = gold, 4 = platinum, 5 = diamond, 6 = master, 7 = grandmaster, 8 = challenger, 9 = unranked)
        #- If we're keeping track of the divison can we have a seperate variable like self.rankDivision I feel like this will be the easiest way to track
        #- For that variable could we make it (1 = division 1, 2 = division 2, 3 = division 3, 4 = division 4)
        #- And it will make it easier for me to graph
