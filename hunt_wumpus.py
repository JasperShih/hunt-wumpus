__author__ = 'Jasper'


class Game:
    def __init__(self, map_bound):
        self.map_bound = map_bound

    def is_valid_location(self, (x, y)):
        if (0 <= x < self.map_bound[0]) & (0 <= y < self.map_bound[1]):
            return True
        else:
            return False


class Creature:
    def __init__(self, game, initial_location):
        self.game = game
        if self.game.is_valid_location(initial_location):
            self.location = initial_location
        else:
            print "Invalid initial location!"
            self.location = (0, 0)

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
