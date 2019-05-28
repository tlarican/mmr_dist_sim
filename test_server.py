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
        for i in range(10):
            server.pick_lobby(model.player_list)
        if SHOW_GRAPHS:
            Graphing.showMMR(model.player_list)
            Graphing.showRanksUnsorted(model.player_list)

    def test_match_winner_handling(self):
        players = server._test_match_winner_handling()
        self.assertEqual(985, players[0].mmr, msg='Player 0 MMR')
        self.assertEqual(0, players[0].lp, msg='Player 0 LP')
        self.assertTrue(players[0].rankDownMatch, msg='Player 0 rankDownMatch')
        self.assertEqual(1975, players[1].mmr, msg='Player 1 MMR')
        self.assertEqual(0, players[1].lp, msg='Player 1 LP')
        self.assertTrue(players[1].rankDownMatch, msg='Player 1 rankDownMatch')
        self.assertEqual(2015, players[5].mmr, msg='Player 5 MMR')
        self.assertEqual(18, players[5].lp, msg='Player 5 LP')
        self.assertEqual(1025, players[6].mmr, msg='Player 6 MMR')
        self.assertEqual(23, players[6].lp, msg='Player 6 LP')
