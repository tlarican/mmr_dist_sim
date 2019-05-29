# -*- coding: utf-8 -*-
import numpy as np
from Player import Player

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
    """
    #-Adds together the players skills that affect the early game for both teams
    
    team_1_earlyGame = np.average(players[:TEAM_SIZE].skill + players[:TEAM_SIZE].lastHitting + \
        players[:TEAM_SIZE].tilt + players[:TEAM_SIZE].waveManagement + players[:TEAM_SIZE].mechanics)
        
    team_2_earlyGame = np.average(players[TEAM_SIZE:].skill + players[TEAM_SIZE:].lastHitting + \
        players[TEAM_SIZE:].tilt + players[TEAM_SIZE:].waveManagement + players[TEAM_SIZE:].mechanics)
    
    
    #-Sets the percent chance to win by dividing it by the amount of skills * 10
    
    team_1_earlyGame = team_1_earlyGame / 50
    team_2_earlyGame = team_2_earlyGame / 50
    
    
    #-
    """

    # - Variable Declarations
    
    team_1_odds = 0
    team_2_odds = 0
    
    
    #- Gets average of skill
    
    for iplayer in players[:TEAM_SIZE]:
        team_1_odds = team_1_odds + iplayer.skill
    for iplayer in players[TEAM_SIZE:]:
        team_2_odds = team_2_odds + iplayer.skill
    team_1_odds = team_1_odds / TEAM_SIZE
    team_2_odds = team_2_odds / TEAM_SIZE 
 
 
    #- Gets the winner    
      
    winner = 1 + (team_1_odds > team_2_odds)


    # - Updates non rank/mmr/lp values

    for i in range(10):
        if (players[i].amountOfGamesPlayed == 8):
            players[i].rankUpMatch = True
        players[i].has_played = True
        players[i].amountOfGamesPlayed += 1

    return winner


def handleMatchResults(players, winner, average_mmr):
    """Takes the results of a match and adjust player mmr, lp, and rank
    
        Variables:
            players = List of players in match
            team_1_odds = The chances that team 1 would win
            team_2_odds = The chances that team 2 would win
            average_mmr = The average mmr of the match     
    """

    # - If team one won (0-4 in array)
    
    if (winner == 2):
        for i in range(TEAM_SIZE):

            # -Determines if the players are above or below average mmr

            if (players[i].mmr < average_mmr):
                if((players[i].mmr + 25) < 2800):
                    players[i].mmr += 25
                if (players[i].rankUpMatch == True):
                    players[i].rankUp()
                elif ((players[i].lp + 23) > 100):
                    players[i].lp = 100
                    players[i].rankUpMatch = True
                else:
                    players[i].lp += 23
                    players[i].rankDownMatch = False
            else:
                if((players[i].mmr + 15) < 2800):
                    players[i].mmr += 15
                if (players[i].rankUpMatch == True):
                    players[i].rankUp()
                elif ((players[i].lp + 18) > 100):
                    players[i].lp = 100
                    players[i].rankUpMatch = True
                else:
                    players[i].lp += 18
                    players[i].rankDownMatch = False
                    
        
        #-Runs through the losing team(5-9)
        
        for i in range(10):
            if (i < 5):
                continue
            if (players[i].mmr < average_mmr):
                if((players[i].mmr - 15) > 0):
                    players[i].mmr -= 15
                if (players[i].rankDownMatch == True):
                    players[i].rankDown()
                elif ((players[i].lp - 18) < 0):
                    players[i].lp = 0
                    players[i].rankDownMatch = True
                else:
                    players[i].lp -= 18
                    players[i].rankUpMatch = False
            else:
                if((players[i].mmr - 24) > 0):
                    players[i].mmr -= 24
                if (players[i].rankDownMatch == True):
                    players[i].rankDown()
                elif ((players[i].lp - 23) < 0):
                    players[i].lp = 0
                    players[i].rankDownMatch = True
                else:
                    players[i].lp -= 23
                    players[i].rankUpMatch = False


    # -If Team 2 won

    else:
        
        #-Runs through winning team (5-9)
        
        for i in range(10):
            if (i < 5):
                continue

            # - Determines if above or below average mmr

            if (players[i].mmr < average_mmr):
                if((players[i].mmr + 25) < 2800):
                    players[i].mmr += 25
                if (players[i].rankUpMatch == True):
                    players[i].rankUp()
                elif ((players[i].lp + 23) > 100):
                    players[i].lp = 100
                    players[i].rankUpMatch = True
                else:
                    players[i].lp += 23
                    players[i].rankDownMatch = False
            else:
                if((players[i].mmr + 15) < 2800):
                    players[i].mmr += 15
                if (players[i].rankUpMatch == True):
                    players[i].rankUp()
                elif ((players[i].lp + 18) > 100):
                    players[i].lp = 100
                    players[i].rankUpMatch = True
                else:
                    players[i].lp += 18
                    players[i].rankDownMatch = False
                    
        
        #-Runs through losing team (0-4)
        
        for i in range(TEAM_SIZE):
            if (players[i].mmr < average_mmr):
                if((players[i].mmr - 15) > 0):
                    players[i].mmr -= 15
                if (players[i].rankDownMatch == True):
                    players[i].rankDown()
                elif ((players[i].lp - 18) < 0):
                    players[i].lp = 0
                    players[i].rankDownMatch = True
                else:
                    players[i].lp -= 18
                    players[i].rankUpMatch = False
            else:
                if((players[i].mmr - 24) > 0):
                    players[i].mmr -= 24
                if (players[i].rankDownMatch == True):
                    players[i].rankDown()
                elif ((players[i].lp - 23) < 0):
                    players[i].lp = 0
                    players[i].rankDownMatch = True
                else:
                    players[i].lp -= 23
                    players[i].rankUpMatch = False

def pick_lobby(all_players):
    """
        Input
        -----
            all_players: np array containing all the players in the simulation
    """
    
    #- Puts all players that are online in a list
    
    online_players = []
    for i in all_players:
        if i.is_online == True:
            online_players.append(i)
    
    
    #-Sorts the players in the list by mmr
    
    online_players.sort(key = lambda x: x.mmr)
    
    
    #-Inserts players into a numpy array
    
    online_players = np.array(online_players)
    ONLINE_COUNT = online_players.size
    
    
    #-Runs the matches
    
    for i in range(round(ONLINE_COUNT / 20)):
        match_1_average_mmr = 0
        match_2_average_mmr = 0
        
        #-Gets top ten players, shuffles them, gets average mmr and winner
        
        teamOne = online_players[:10]
        np.random.shuffle(teamOne)
        match_1_result = match(teamOne)
        for i in range(10):
            match_1_average_mmr = match_1_average_mmr + teamOne[i].mmr
        
        match_1_average_mmr = match_1_average_mmr / 10
        handleMatchResults(teamOne, match_1_result, \
                           match_1_average_mmr)
        
        
        #-Gets bottom ten players, shuffles them, gets average mmr and winner
        
        teamTwo = online_players[-10:]
        np.random.shuffle(teamTwo)
        match_2_result = match(teamTwo)
        
        for i in range(10):
            match_2_average_mmr = match_2_average_mmr +teamTwo[i].mmr
            
        match_2_average_mmr = match_2_average_mmr / 10 
        handleMatchResults(teamTwo, match_2_result, \
                           match_2_average_mmr)
        
        
        #-Shrinks array so that players that played are not in it
        
        online_players = online_players[10:-10]
     
           
    #-If there are more than ten players left who haven't played
    
    if(online_players.size >= 10):
        match_average_mmr = 0
        
        #-Gets top ten players, shuffles them, gets average mmr and winner
        
        teamThree = online_players[:10]
        np.random.shuffle(teamThree)
        match_result = match(teamThree)
        
        for i in range(10):
            match_average_mmr = match_average_mmr +teamThree[i].mmr
            
        match_average_mmr = match_average_mmr / 10
        handleMatchResults(teamThree, match_result, \
                           match_average_mmr)
        
        online_players = online_players[10:]
        
    return online_players

def _test_match_winner_handling():
    player_list = []
    for i in range(10):
        player_list.append(Player())
    player_list[0].mmr = 1000
    player_list[1].mmr = 2000
    player_list[2].mmr = 1000
    player_list[3].mmr = 2000
    player_list[4].mmr = 1000
    player_list[5].mmr = 2000
    player_list[6].mmr = 1000
    player_list[7].mmr = 2000
    player_list[8].mmr = 1000
    player_list[9].mmr = 2000
    for i in range(10):
        handleMatchResults(player_list, 1, 1500)
    return player_list
