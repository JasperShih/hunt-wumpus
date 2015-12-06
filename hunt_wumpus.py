# -*- coding: utf8 -*-
__author__ = 'Jasper'

class Game:
    def __init__(self, game_map, player, wumpus):
        self.game_map =game_map
        self.player =player
        self.wumpus = wumpus

        self.locate(self.player)
        self.locate(self.wumpus)

    def locate(self, creature):
        if self.game_map.is_valid_location(creature.initial_location):
            creature.location = creature.initial_location
        else:
            print "Invalid initial location!"
            creature.location = (0,0)

    def is_defeat(self):
        if self.player.get_location() == self.wumpus.get_location():
            return True
        else:
            return False



class Map:
    def __init__(self, map_bound):
        self.map_bound = map_bound

    def is_valid_location(self, (x, y)):
        if (0 <= x < self.map_bound[0]) & (0 <= y < self.map_bound[1]):
            return True
        else:
            return False


class Creature:
    def __init__(self, initial_location):
        self.initial_location = initial_location
        self.location = None

    def move(self, direction):
        if direction == "up":
            self.update_location((0, -1))
        elif direction == "down":
            self.update_location((0, 1))
        elif direction == "left":
            self.update_location((-1, 0))
        elif direction == "right":
            self.update_location((1, 0))
        else:
            print "Invalid direction input!"
            # arise exception

    def update_location(self, offset):
        new_location = (self.location[0] + offset[0],
                        self.location[1] + offset[1])
        if self.game.is_valid_location(new_location):
            self.location = new_location
        else:
            # Remain self.location = its original value
            pass

    def get_location(self):
        return self.location

class Player(Creature):
    def attack(self, direction):
        if direction == "up":
            self.kill_wumpus((0, -1))
        elif direction == "down":
            self.update_location((0, 1))
        elif direction == "left":
            self.update_location((-1, 0))
        elif direction == "right":
            self.update_location((1, 0))
        else:
            print "Invalid direction input!"
            # arise exception

    def kill_wumpus(self, offest):
        player_location = self.get_location()
        if (player_location[0]+offest[0], player_location[1]+offest[1])


if __name__ == '__main__':
    pass


# 要從Game, map, creature開始寫