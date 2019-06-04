# =======================================================================
#                           General Documentation

"""
Tests for Server Class
"""

# ---------------- Module General Import and Declarations ---------------
import server
from Model import Model
import Graphing

SHOW_GRAPHS = True


class Tests(object):
    """
    Testing object for when test.py is ran through main
    """

    def test_one_round(self):
        model = Model()
        server.pick_lobby(model.player_list)
        if SHOW_GRAPHS:
            Graphing.showMMR(model.player_list)
            Graphing.showRanksUnsorted(model.player_list)

    def test_multiple_rounds(self):
        model = Model()
        model.player_list[0].createUserPlayer(6, 6, 6, 6,
                         6, 6, 6, 6,
                         6)
        for i in range(1000):
            server.pick_lobby(model.player_list)
        if SHOW_GRAPHS:
            Graphing.showMMR(model.player_list)
            Graphing.showRanksUnsorted(model.player_list)
            Graphing.showPlayerStats(model.player_list)
        model.to_csv()

    def test_match_winner_handling(self):
        players = server._test_match_winner_handling()
        self.assertEqual(1517, players[0].mmr, msg='Win Below MMR')
        self.assertEqual(87, players[0].lp, msg='Win Below LP')
        self.assertEqual(1562, players[1].mmr, msg='Win Above MMR')
        self.assertEqual(16, players[1].lp, msg='Win Above LP')
        self.assertEqual(100, players[2].lp, msg='At Rank Up LP')
        self.assertTrue(players[2].rankUpMatch, msg='At Rank Up Bool')
        self.assertEqual(5, players[3].rank, msg='Rank Up Rank')
        self.assertEqual(4, players[3].rankDivision, msg='Rank Up Division')
        self.assertEqual(0, players[3].lp, msg='Rank Up LP')
        self.assertFalse(players[3].rankUpMatch, msg='Rank Up Bool')
        self.assertEqual(1483, players[5].mmr, msg='Lose Above MMR')
        self.assertEqual(0, players[5].lp, msg='Lost Above LP')
        self.assertEqual(1438, players[6].mmr, msg='Lose Below MMR')
        self.assertEqual(37, players[6].lp, msg='Lose Below LP')
        self.assertEqual(0, players[7].lp, msg='At Rank Down LP')
        self.assertTrue(players[7].rankDownMatch, msg='At Rank Down Bool')
        self.assertEqual(2, players[8].rank, msg='Rank Down Rank')
        self.assertEqual(4, players[8].rankDivision, msg='Rank Down Division')
        self.assertEqual(30, players[8].lp, msg='Rank Down LP')
        self.assertFalse(players[8].rankDownMatch, msg='Rank Down Bool')
