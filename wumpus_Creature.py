from abc import ABCMeta
import msvcrt


class Creature:
    __metaclass__ = ABCMeta
    UP = 119
    DOWN = 115
    LEFT = 97
    RIGHT = 100
    move_directions = [UP, DOWN, LEFT, RIGHT]

    def __init__(self):
        self.location = None


class Player(Creature):
    CTRL_UP = 23
    CTRL_DOWN = 19
    CTRL_LEFT = 1
    CTRL_RIGHT = 4
    attack_directions = [CTRL_UP, CTRL_DOWN, CTRL_LEFT, CTRL_RIGHT]

    def __init__(self):
        super(Player, self).__init__()
        self.action = None

    def get_action(self):
        action_buffer = None
        while Player.is_not_valid_action(action_buffer):
            print "Input valid action:"
            action_buffer = ord(msvcrt.getch())
        self.action = action_buffer
    """
    def get_action2(self):
        self.action = msvcrt.getch()
        if Player.is_not_valid_action(self.action):
            self.get_action2()
    """

    @staticmethod
    def is_not_valid_action(action_buffer):
        return (True if (action_buffer not in (Player.move_directions +
                                               Player.attack_directions))else
                False)

    def is_attack_action(self):
        return (True if (self.action in Player.attack_directions) else
                False)


class Wumpus(Creature):
    pass

