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

    team_1_skill_agg = 0
    team_2_skill_agg = 0

    # - Gets average of skill

    for iplayer in players[:TEAM_SIZE]:
        team_1_skill_agg = 3 * np.random.normal(1, .05) * iplayer.communication + \
                           2 * np.random.normal(1, .05) * iplayer.tilt + \
                           2 * np.random.normal(1, .05) * iplayer.internet + \
                           3 * np.random.normal(1, .05) * iplayer.leadership + \
                           3 * np.random.normal(1, .05) * iplayer.gameKnowledge + \
                           np.random.normal(1, .05) * iplayer.reactionTimes + \
                           4 * np.random.normal(1, .05) * iplayer.early_game + \
                           4 * np.random.normal(1, .05) * iplayer.late_game + \
                           5 * np.random.normal(1, .05) * iplayer.mechanics
    for iplayer in players[TEAM_SIZE:]:
        team_2_skill_agg = 3 * np.random.normal(1, .05) * iplayer.communication + \
                           2 * np.random.normal(1, .05) * iplayer.tilt + \
                           2 * np.random.normal(1, .05) * iplayer.internet + \
                           3 * np.random.normal(1, .05) * iplayer.leadership + \
                           3 * np.random.normal(1, .05) * iplayer.gameKnowledge + \
                           np.random.normal(1, .05) * iplayer.reactionTimes + \
                           4 * np.random.normal(1, .05) * iplayer.early_game + \
                           4 * np.random.normal(1, .05) * iplayer.late_game + \
                           5 * np.random.normal(1, .05) * iplayer.mechanics

    # - Gets the winner

    winner = 1 + (team_1_skill_agg > team_2_skill_agg)

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
            winner = Indicates which team won, 2 for team 1, 1 for team 2
            average_mmr = The average mmr of the match
    """
    if (winner == 2):
        # -Determines if the players are above or below average mmr      
        # -Runs through the losing team(5-9)
        for i in range(TEAM_SIZE * 2):
            if (i < TEAM_SIZE):
                handleMatchResultsHelper(players[i], average_mmr, 1)
            else:
                handleMatchResultsHelper(players[i], average_mmr, -1)
    # -If Team 2 won
    else:
        # -Runs through winning team (5-9)
        # - Determines if above or below average mmr       
        # -Runs through losing team (0-4)
        for i in range(TEAM_SIZE * 2):
            if (i < TEAM_SIZE):
                handleMatchResultsHelper(players[i], average_mmr, -1)
            else:
                handleMatchResultsHelper(players[i], average_mmr, 1)


def handleMatchResultsHelper(player, average_mmr, gamePosition):
    # -Determines if the players are above or below average mmr
    mmr_difference = player.mmr - average_mmr

    if(gamePosition == -1 and mmr_difference >= 0):
        mmr_difference = (mmr_difference * -2) / 1.5
    elif(gamePosition == -1 and mmr_difference < 0):
        mmr_difference = (-300 - mmr_difference) / 20
    elif(gamePosition == 1 and mmr_difference >= 0):
        mmr_difference = (300 - mmr_difference) / 20
    else:
        mmr_difference = (mmr_difference * -2) / 1.5
      
    if(0 < player.mmr + mmr_difference < 2800):  
        player.mmr += mmr_difference
    checkMatch(player, gamePosition, mmr_difference)


def checkMatch(player, gamePosition, lpChange):
    if(player.amountOfGamesPlayed < 10):
        return
    elif(player.amountOfGamesPlayed == 10):
        player.rankUp()
    elif (gamePosition < 0):
        if (player.rankDownMatch == True):
            player.rankDown()
        elif (player.lp + lpChange < 0):
            player.lp = 0
            player.rankDownMatch = True
        else:
            player.lp += 1.05 * round(lpChange)
            player.rankUpMatch = False
    else:
        if (player.rankUpMatch == True):
            player.rankUp()
        elif (player.lp + lpChange > 100):
            player.lp = 100
            player.rankUpMatch = True
        else:
            player.lp += 1.3 * round(lpChange)
            player.rankDownMatch = False


def pick_lobby(all_players):
    """
        Input
        -----
            all_players: np array containing all the players in the simulation
    """

    # - Puts all players that are online in a list

    online_players = []
    for i in all_players:
        if i.is_online == True:
            online_players.append(i)

    # -Sorts the players in the list by mmr

    online_players.sort(key=lambda x: x.mmr)

    # -Inserts players into a numpy array

    online_players = np.array(online_players)
    ONLINE_COUNT = online_players.size

    # -Runs the matches

    for i in range(round(ONLINE_COUNT / 20)):
        match_1_average_mmr = 0
        match_2_average_mmr = 0

        # -Gets top ten players, shuffles them, gets average mmr and winner

        teamOne = online_players[:10]
        np.random.shuffle(teamOne)
        match_1_result = match(teamOne)
        for i in range(10):
            match_1_average_mmr = match_1_average_mmr + teamOne[i].mmr

        match_1_average_mmr = match_1_average_mmr / 10
        handleMatchResults(teamOne, match_1_result, \
                           match_1_average_mmr)

        # -Gets bottom ten players, shuffles them, gets average mmr and winner

        teamTwo = online_players[-10:]
        np.random.shuffle(teamTwo)
        match_2_result = match(teamTwo)

        for i in range(10):
            match_2_average_mmr = match_2_average_mmr + teamTwo[i].mmr

        match_2_average_mmr = match_2_average_mmr / 10
        handleMatchResults(teamTwo, match_2_result, \
                           match_2_average_mmr)

        # -Shrinks array so that players that played are not in it

        online_players = online_players[10:-10]

    # -If there are more than ten players left who haven't played

    if (online_players.size >= 10):
        match_average_mmr = 0

        # -Gets top ten players, shuffles them, gets average mmr and winner

        teamThree = online_players[:10]
        np.random.shuffle(teamThree)
        match_result = match(teamThree)

        for i in range(10):
            match_average_mmr = match_average_mmr + teamThree[i].mmr

        match_average_mmr = match_average_mmr / 10
        handleMatchResults(teamThree, match_result, \
                           match_average_mmr)

        online_players = online_players[10:]

    return online_players


def _test_match_winner_handling():
    player_list = []
    for i in range(10):
        player_list.append(Player())

    #  Winning below MMR average

    player_list[0].mmr = 1450
    player_list[0].rank = 2
    player_list[0].rankDivision = 3

    #  Winning above MMR average

    player_list[1].mmr = 1550
    player_list[1].rank = 4
    player_list[1].rankDivision = 1

    #  100 LP

    player_list[2].mmr = 1450
    player_list[2].rank = 2
    player_list[2].rankDivision = 3
    player_list[2].lp = 99

    #  Require Rank Up

    player_list[3].mmr = 1550
    player_list[3].rank = 4
    player_list[3].rankDivision = 1
    player_list[3].rankUpMatch = True
    player_list[3].amountOfGamesPlayed = 20

    player_list[4].mmr = 1450

    #  Losing below MMR average

    player_list[5].mmr = 1550
    player_list[5].rank = 4
    player_list[5].rankDivision = 1
    player_list[5].lp = 50

    #  Losing above MMR average

    player_list[6].mmr = 1450
    player_list[6].rank = 2
    player_list[6].rankDivision = 3
    player_list[6].lp = 50

    #  0 LP

    player_list[7].mmr = 1550
    player_list[7].rank = 4
    player_list[7].rankDivision = 1
    player_list[7].lp = 1

    #  Require rank down

    player_list[8].mmr = 1450
    player_list[8].rank = 2
    player_list[8].rankDivision = 3
    player_list[8].rankDownMatch = True
    player_list[8].amountOfGamesPlayed = 20

    player_list[9].mmr = 1550

    handleMatchResults(player_list, 2, 1500)
    return player_list
