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
    """
    def test_one_round(self):
        model = Model()
        server.pick_lobby(model.player_list)
        if SHOW_GRAPHS:
            Graphing.showMMR(model.player_list)
            Graphing.showRanksUnsorted(model.player_list)
        """
    def test_multiple_rounds(self):
        model = Model()
        for i in range(100):
            server.pick_lobby(model.player_list)
        if SHOW_GRAPHS:
            Graphing.showMMR(model.player_list)
            Graphing.showRanksUnsorted(model.player_list)
