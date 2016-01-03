import random
from wumpus_Creature import Creature, Player

__author__ = 'Jasper'


class Game:
    def __init__(self, arena, player, wumpus):
        self.arena = arena
        self.player = player
        self.wumpus = wumpus
        self.turns = 0

        self.locate_on_arena(self.player, 'P')
        self.locate_on_arena(self.wumpus, 'W')

    def locate_on_arena(self, creature, character):
        spawn_row = random.randrange(0, self.arena.row_limit)
        spawn_col = random.randrange(0, self.arena.col_limit)
        if self.arena.array[spawn_row][spawn_col] == '-':
            self.arena.array[spawn_row][spawn_col] = character
            creature.location = (spawn_row, spawn_col)
        else:  # Avoid to locate player and wumpus on same location
            self.locate_on_arena(creature, character)

    def move(self, creature):
        offset = self.move_offset(creature)
        after_location = (offset[0] + creature.location[0],
                          offset[1] + creature.location[1])
        if self.is_in_arena(after_location):
            character = ('P' if (creature is self.player) else
                         'W')
            self.update_creature(creature, after_location, character)
        else:
            print "Encounter wall!"

    def move_offset(self, creature):
        direction = ([self.player.action] if (creature is self.player) else
                     [random.choice([Creature.UP, Creature.DOWN, Creature.LEFT, Creature.RIGHT])])

        offset = map(lambda element: (-1, 0) if (element is Creature.UP)else
                                     (1, 0) if (element is Creature.DOWN)else
                                     (0, -1) if (element is Creature.LEFT)else
                                     (0, 1),
                     direction)
        return offset[0]  # [(1,0)]
        # return *offset

    def is_in_arena(self, after_location):
        return (after_location[0] in [i for i in xrange(0, self.arena.row_limit)]) and \
               (after_location[1] in [i for i in xrange(0, self.arena.col_limit)])
        # new_location in [(i, j) for i in xrange(0, 3) for j in xrange(0, 3)]

    def update_creature(self, creature, after_location, character):
        self.arena.array[creature.location[0]][creature.location[1]] = '-'
        if self.arena.array[after_location[0]][after_location[1]] is '-':
            self.arena.array[after_location[0]][after_location[1]] = character
            creature.location = after_location
        else:
            self.player = None

    def attack(self, attacker, target):
        offset = map(lambda element: (-1, 0) if (element is Player.CTRL_UP)else
                                     (1, 0) if (element is Player.CTRL_DOWN)else
                                     (0, -1)if (element is Player.CTRL_LEFT)else
                                     (0, 1),
                     [self.player.action])

        after_location = (offset[0][0] + self.player.location[0],
                          offset[0][1] + self.player.location[1])

        if self.is_in_arena(after_location):
            if self.arena.array[after_location[0]][after_location[1]] is 'W':
                self.wumpus = None
            else:
                print "Attack miss"
        else:
            print "Hit wall"



























