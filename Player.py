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
