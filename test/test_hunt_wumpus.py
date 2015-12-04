__author__ = 'Jasper'

import unittest
from hunt_wumpus import *


class HuntWumpusTest(unittest.TestCase):
    # Setting up before any test cases run
    def setUp(self):
        pass

    # Tear down after any test cases end
    def tearDown(self):
        pass

    def test_map(self):
        # In this case, map size is (0~9) * (0-9)
        map_bound = (10, 10)
        game = Game(map_bound)
        self.assertEqual(game.is_valid_location((5, 8)), True)
        self.assertEqual(game.is_valid_location((10, 4)), False)

    def test_move(self):
        game = Game((5, 5))
        initial_location = (3, 2)
        player = Creature(game, initial_location)
        player.move("up")
        self.assertEqual(player.get_location(), (3, 1))

    def test_defeat(self):
        pass

    def test_win(self):
        pass


if __name__ == '__main__':
    unittest.main()

