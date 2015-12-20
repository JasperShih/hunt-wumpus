# -*- coding: utf8 -*-
__author__ = 'Jasper'
import msvcrt


class Game:
    move_directions = ['w', 's', 'a', 'd']
    attack_directions = ['\x17', '\x13', '\x01', '\x04']

    def __init__(self, game_map, player, wumpus):
        self.game_map = game_map
        self.player = player
        self.wumpus = wumpus
        self.turn = 0

        self.locate(self.player)
        self.locate(self.wumpus)

    def run(self):
        while ~self.is_game_end():
            self.do_turn()
        display_score()

    def is_game_end(self):
        if self.wumpus is None or \
           self.player is None:
            game_end = True
        else:
            game_end = False
        return game_end

    def do_turn(self):
        active_role = self.get_active_role()
        if active_role == "player":
            self.player_act()
        else:
            self.wumpus_act()
        self.turn += 1

    def get_active_role(self):
        if self.turn % 2 == 0:
            role = "player"
        else:
            role = "wumpus"
        return role

    def player_act(self):
        action = Game.get_action()
        self.conduct(action)

    def conduct(self, action):
        if action in Game.move_directions:
            move_direction = action
            self.player.move(move_direction)
            if self.meet(self.player.get_location(),
                         self.wumpus.get_location()):
                self.player = None
        else:
            attack_direction = action
            if self.meet(self.player.get_location() + attack_direction,
                         self.wumpus.get_location()):
                self.wumpus = None

    @staticmethod
    def meet(location1, location2):
        if location1 == location2:
            result = True
        else:
            result = False
        return result
#============================================================================
    def wumpus_act(self):
        self.wumpus.move(random_direction)


    def update_game_states(self):
        pass

    @staticmethod
    def get_action():
        action_key = None
        while ~Game.is_corrected_key(action_key):
            action_key = msvcrt.getch()
        return action_key

    @staticmethod
    def is_corrected_key(action_key):
        if action_key in (Game.move_directions + Game.attack_directions):
            result = True
        else:
            result = False
        return result

    def locate(self, creature):
        if self.game_map.is_valid_location(creature.initial_location):
            creature.location = creature.initial_location
        else:
            print "Invalid initial location!"
            creature.location = (0, 0)

    def is_defeat(self):
        if self.player.get_location() == self.wumpus.get_location():
            return True
        else:
            return False

    def attack_judgment(self, attacker, direction, target):
        attacker_location = attacker.get_location()
        attack_area = self.update_location(attacker_location, direction)

        result = None
        if attack_area == target.get_location():
            result = "hit"
        else:
            result = "miss"
        return result

    def update_location(self, location, direction):
        offset = None
        if direction == "up":
            offset = (0, -1)
        elif direction == "down":
            offset = (0, 1)
        elif direction == "left":
            offset = (-1, 0)
        elif direction == "right":
            offset = (1, 0)
        else:
            print "Invalid direction input!"
            # arise exception

        new_location = (location[0] + offset[0],
                        location[1] + offset[1])
        if self.game_map.is_valid_location(new_location):
            updated_location = new_location
        else:
            updated_location = location

        return updated_location

    def is_win(self):
        result = None
        if self.wumpus:
            result = False
        else:
            result = True
        return result


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


if __name__ == '__main__':
    pass


    # 要從Game, map, creature開始寫
