# -*- coding: utf8 -*-
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
        game_map = Map(map_bound)
        self.assertEqual(game_map.is_valid_location((5, 8)), True)
        self.assertEqual(game_map.is_valid_location((10, 4)), False)

    # unfinished
    def test_move(self):
        game_map = Map((5, 5))
        # initial_location
        player = Creature((3, 2))
        wumpus = Creature((1, 0))
        game = Game(game_map, player, wumpus)

        game.player.move("up")
        game.wumpus.move("left")
        self.assertEqual(game.player.get_location(), (3, 1))
        self.assertEqual(game.wumpus.get_location(), (1, 0))

    def test_defeat(self):
        game_map = Map((5, 5))
        # initial_location
        player = Creature((3, 3))
        wumpus = Creature((3, 3))
        game = Game(game_map, player, wumpus)

        self.assertEqual(game.is_defeat(), True)

    def test_win(self):
        game_map = Map((5, 5))
        # initial_location
        player = Creature((3, 2))
        wumpus = Creature((3, 3))
        game = Game(game_map, player, wumpus)

        game.player.attack("right")
        # game.wumpus = None

        self.assertEqual(game.is_win(), True)



if __name__ == '__main__':
    unittest.main()

"""
心得:
Instructive programming
要從defeat/win->map->move的順序由小到大開始寫 (Top->Down)
才不會一直架構要重改

win 和move 還沒寫
"""
