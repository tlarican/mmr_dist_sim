# =======================================================================
#                           General Documentation

"""Module that contains player class
"""

# ---------------- Module General Import and Declarations ---------------

import unittest
from Model import Model
from Player import Player
import test_model
import test_player
import test_server
import test_graphing


class SetUpTest(unittest.TestCase):
    def setUp(self):
        self.string_test = "Hello There"


class ModelTests(SetUpTest, test_model.Tests): pass


class PlayerTests(SetUpTest, test_player.Tests): pass


class ServerTests(SetUpTest, test_server.Tests): pass


class GraphingTests(SetUpTest, test_graphing.Tests):pass


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ModelTests))
    suite.addTest(unittest.makeSuite(PlayerTests))
    suite.addTest(unittest.makeSuite(ServerTests))
    suite.addTest(unittest.makeSuite(GraphingTests))
    unittest.TextTestRunner().run(suite)
