# =======================================================================
#                           General Documentation

"""
Tests for Player Class
"""

# ---------------- Module General Import and Declarations ---------------
from Player import Player


class Tests(object):
    """
    Testing object for when test.py is ran through main
    """
    def test_player_init(self):
        player = Player()
        self.assertEqual(player.mmr, 1500)
        self.assertTrue(player.rankUpMatch is False)
        self.assertTrue(player.rankDownMatch is False)
        self.assertTrue(player.has_played is False)
        self.assertEqual(player.amountOfGamesPlayed, 0)
        self.assertEqual(player.lp, 0)
        self.assertTrue(player.is_online is True)
        self.assertEqual(player.rank, 9)
        self.assertEqual(player.rankDivision, 1)
        self.assertEqual(player.lp, 1000)

    def test_player_ranking(self):
        """
        Starting from lowest rank and division, rank to highest rank and division
        From highest rank and division, derank to lowest rank and division
        Makes sure every line of code in rankUp and rankDown is touched
        """
        player = Player()
        player.amountOfGamesPlayed = 10
        ranks = player._test_rank_methods()
        self.assertEqual(ranks, (8, 1, 0, 4), msg='Player Ranking Failed')
