import unittest
from Model import Model
from tests import test_model


class SetUpTest(unittest.TestCase):
    def setUp(self):
        self.string_test = "Hello There"
        self.modelobj = Model()


class ModelTests(SetUpTest, test_model.Tests): pass


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ModelTests))
    # suite.addTest(unittest.makeSuite(PlayerTests))
    unittest.TextTestRunner().run(suite)

