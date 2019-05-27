# -*- coding: utf-8 -*-
"""
Created on Tue May 21 21:23:28 2019

@author: atche
"""

import numpy as np

TEAM_SIZE = 5

def match(players):
    """
        Input
        -----
            players: a 10-element array that contains the 10 players in a 
            match. The first 5 are on one team and the last 5 are on the other.
        Output
        ------
            returns 1 if team 1 wins, otherwise 2
    """
    team_1_odds = np.average(players[:TEAM_SIZE].skill)
    team_2_odds = np.average(players[TEAM_SIZE:].skill)
    
    return 1 + (team_2_odds > team_1_odds)

def pick_lobby(all_players):
    """
        Input
        -----
            all_players: np array containing all the players in the simulation
    """
    online_players = []
    for i in all_players:
        if i.is_online == True:
            online_players.append(i)
    
    online_players.sort(key = lambda x: x.mmr)
    online_players = np.array(online_players)
    ONLINE_COUNT = online_players.size()
    for i in ONLINE_COUNT / 20:
        match_1_result = match(online_players[:10])
        match_2_result = match(online_players[-10:])
        #do something about the results (MMR and rank function)
        online_players = online_players[10:-10]
        
    #at this point the array should have less than 20 elements
    if(online_players.size() >= 10):
        match_result = match(online_players[:10])
        #do something about the results (MMR and rank function)

    