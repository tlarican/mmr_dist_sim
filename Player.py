import numpy as np


class Player(object):
    """Create and manage Player variables and attributes
    
        Variables:
            skill: Temp variable to quantify skill of player
            mmr: Current MMR of player
    """

    def __init__(self, mmr_default=1400):
        self.skill = np.random.normal(5, 2)
        self.mmr = mmr_default
