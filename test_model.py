# =======================================================================
#                           General Documentation

"""
Tests for Model Class
"""

# ---------------- Module General Import and Declarations ---------------
from Model import Model


class Tests(object):
    """
    Testing object for when test.py is ran through main
    """
    def test_model_init(self):
        model = Model()
        self.assertEqual(model._test_player_list_size(), 1000)


