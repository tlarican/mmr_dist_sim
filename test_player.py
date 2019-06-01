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
        self.assertEqual(player.lp, 0)

    def test_player_ranking(self):
        """
        Starting from lowest rank and division, rank to highest rank and division
        From highest rank and division, derank to lowest rank and division
        Makes sure every line of code in rankUp and rankDown is touched
        """
        player = Player()
        ranks = player._test_rank_min_max()
        self.assertEqual((8, 1, 0, 4), ranks, msg='Player Ranking Failed')
        ranks = player._test_placements(60)
        self.assertEqual((0, 4), ranks, msg='Bucket 1 Failed')
        ranks = player._test_placements(170)
        self.assertEqual((0, 3), ranks, msg='Bucket 2 Failed')
        ranks = player._test_placements(320)
        self.assertEqual((0, 2), ranks, msg='Bucket 3 Failed')
        ranks = player._test_placements(390)
        self.assertEqual((0, 1), ranks, msg='Bucket 4 Failed')
        ranks = player._test_placements(510)
        self.assertEqual((1, 4), ranks, msg='Bucket 5 Failed')
        ranks = player._test_placements(620)
        self.assertEqual((1, 3), ranks, msg='Bucket 6 Failed')
        ranks = player._test_placements(699)
        self.assertEqual((1, 2), ranks, msg='Bucket 7 Failed')
        ranks = player._test_placements(849)
        self.assertEqual((1, 1), ranks, msg='Bucket 8 Failed')
        ranks = player._test_placements(851)
        self.assertEqual((2, 4), ranks, msg='Bucket 9 Failed')
        ranks = player._test_placements(970)
        self.assertEqual((2, 3), ranks, msg='Bucket 10 Failed')
        ranks = player._test_placements(1111)
        self.assertEqual((2, 2), ranks, msg='Bucket 11 Failed')
        ranks = player._test_placements(1189)
        self.assertEqual((2, 1), ranks, msg='Bucket 12 Failed')
        ranks = player._test_placements(1251)
        self.assertEqual((3, 4), ranks, msg='Bucket 13 Failed')
        ranks = player._test_placements(1351)
        self.assertEqual((3, 3), ranks, msg='Bucket 14 Failed')
        ranks = player._test_placements(1549)
        self.assertEqual((3, 2), ranks, msg='Bucket 15 Failed')
        ranks = player._test_placements(1649)
        self.assertEqual((3, 1), ranks, msg='Bucket 16 Failed')
        ranks = player._test_placements(1651)
        self.assertEqual((4, 4), ranks, msg='Bucket 17 Failed')
        ranks = player._test_placements(1751)
        self.assertEqual((4, 3), ranks, msg='Bucket 18 Failed')
        ranks = player._test_placements(1860)
        self.assertEqual((4, 2), ranks, msg='Bucket 19 Failed')
        ranks = player._test_placements(2000)
        self.assertEqual((4, 1), ranks, msg='Bucket 20 Failed')
        ranks = player._test_placements(2100)
        self.assertEqual((5, 4), ranks, msg='Bucket 21 Failed')
        ranks = player._test_placements(2200)
        self.assertEqual((5, 3), ranks, msg='Bucket 22 Failed')
        ranks = player._test_placements(2300)
        self.assertEqual((5, 2), ranks, msg='Bucket 23 Failed')
        ranks = player._test_placements(2400)
        self.assertEqual((5, 1), ranks, msg='Bucket 24 Failed')
        ranks = player._test_placements(2500)
        self.assertEqual((6, 1), ranks, msg='Bucket 25 Failed')
        ranks = player._test_placements(2600)
        self.assertEqual((7, 1), ranks, msg='Bucket 26 Failed')
        ranks = player._test_placements(3000)
        self.assertEqual((8, 1), ranks, msg='Challenger Failed')


