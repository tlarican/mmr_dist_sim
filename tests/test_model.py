from Model import Model

class Tests(object):
    def test_model_init(self):
        model = Model()
        self.assertTrue(model._test_player_list_size() == 1000)
