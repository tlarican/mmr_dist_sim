#=======================================================================
#                           General Documentation

"""Module that contains player class

    see function docstring for description
"""

#---------------- Module General Import and Declarations ---------------

import numpy as np

#-------------------- Class: Player ------------------------------------

#  TODO(Tyler): Create Player Tests
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
        #  TODO(Antong): Make this variable a random number based on what you believe the distribution should be
        self.is_online = True
        #  TODO(Tyler): Make this based off the buckets that will be defined in the Model Object
        self.rank = 9
        self.rankDivision = 1
        #- Connor - For this rank can you use ints? (0 = iron, 1 = bronze, 2 = silver, 3 = gold, 4 = platinum, 5 = diamond, 6 = master, 7 = grandmaster, 8 = challenger, 9 = unranked)
        #- If we're keeping track of the divison can we have a seperate variable like self.rankDivision I feel like this will be the easiest way to track
        #- For that variable could we make it (1 = division 1, 2 = division 2, 3 = division 3, 4 = division 4)
        #- And it will make it easier for me to graph
    

#-------------------- Function: rankUp ------------------------------------   
   
    def rankUp(self):
        """Allows the player to rank up and assigns rank based on mmr
        
            Variables:
                Bucket: Represents bucket of what rank they fall in
                    based on their mmr
        """
        
        #-Variable Declaration
            
        bucket = 100
        
        
        #-If currently unranked
        
        if(self.rank == 9):
            
            
            #-Finds correct bucket by looping
            
            while(self.mmr / bucket > 1):
                bucket += 100
            
        
            #-Makes bucket a smaller number and easier to handle
        
            bucket = bucket / 100
        
        
            #-Finds the rank based off bucket and places it.
        
            if(bucket == 1):
                self.rank = 0
                self.divison = 4
            elif(bucket == 2):
                self.rank = 0
                self.division = 3
            elif(bucket == 3):
                self.rank = 0
                self.division = 2
            elif(bucket == 4):
                self.rank = 0
                self.division = 1
            elif(bucket == 5):
                self.rank = 1
                self.division = 4
            elif(bucket == 6):
                self.rank = 1
                self.division = 3
            elif(bucket == 7):
                self.rank = 1
                self.division = 2
            elif(bucket == 8):
                self.rank = 1
                self.division = 1
            elif(bucket == 9):
                self.rank = 2
                self.division = 4
            elif(bucket == 10):
                self.rank = 2
                self.division = 3
            elif(bucket == 11):
                self.rank = 2
                self.division = 2
            elif(bucket == 12):
                self.rank = 2
                self.division = 1
            elif(bucket == 13):
                self.rank = 3
                self.division = 4
            elif(bucket == 14):
                self.rank = 3
                self.division = 3
            elif(bucket == 15):
                self.rank = 3
                self.division = 2
            elif(bucket == 16):
                self.rank = 3
                self.division = 1
            elif(bucket == 17):
                self.rank = 4
                self.division = 4
            elif(bucket == 18):
                self.rank = 4
                self.division = 3
            elif(bucket == 19):
                self.rank = 4
                self.division = 2        
            elif(bucket == 20):
                self.rank = 4
                self.division = 1
            elif(bucket == 21):
                self.rank = 5
                self.division = 4
            elif(bucket == 22):
                self.rank = 5
                self.division = 3
            elif(bucket == 23):
                self.rank = 5
                self.division = 2
            elif(bucket == 24):
                self.rank = 5
                self.division = 1
            elif(bucket == 25):
                self.rank = 6
                self.division = 1
            elif(bucket == 26):
                self.rank = 7
                self.division = 1
            elif(bucket == 27):
                self.rank = 8
                self.division = 1
         
         
        #-If currently ranked
         
        else:
            
            #-If below master
            
            if(self.rank < 6):
                if(self.division == 1):
                    self.rank += 1
                    self.division = 4
                else:
                    self.division -= 1
                    
            #- If below challenger
                    
            elif(self.rank < 8):
                self.rank += 1
                
            #- If Challenger
                
            else:
                self.rank = 8
                
        self.rankUpMatch = False
        self.lp = 0 
        
#-------------------- Function: rankUp ------------------------------------   

    def rankDown(self):
       """Moves the player down in ranks
       """     
       
       if(self.rank < 6):
           if(self.division == 4 and self.rank == 0):
               self.rank = 0
           elif(self.division == 4):
                self.rank -= 1
                self.division = 1
           else:
                self.division -= 1
       else:
           self.rank -= 1
           self.division = 1
       
       self.rankDownMatch = False
       self.lp = 50
       
       
       
       
       