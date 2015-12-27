# -*- coding: utf8 -*-
from abc import ABCMeta, abstractmethod


class Flow:
    __metaclass__ = ABCMeta

    # 在base abstract class初始化member variable,
    # 因為member variable僅能在 member method中設置
    # (為了在之後inherit Flow的class們,
    # 能夠ref到該member variable, 這case才在base類初始化)
    def __init__(self, game):
        self.game = game

    @abstractmethod
    def procedure_flow(self):
        """
        while is_game_over() is False:
            turn_flow()
        display_score()
        """

    @abstractmethod
    def turn_flow(self):
        """
        active_role = get_active_role()
        active_role.act()
        self.game.turns += 1
        """


class ProcedureFlow(Flow):
    def procedure_flow(self):
        while self.is_game_over() is False:
            self.turn_flow()
        self.display_score()

    def is_game_over(self):
        if None in (self.game.wumpus, self.game.player):
            result = True
        else:
            result = False
        return result

    def display_score(self):
        print "Player:   " + str(self.game.player)
        print "Wumpus:   " + str(self.game.wumpus)
        print "Turns :   " + str(self.game.turns)


class TurnFlow(Flow):
    def turn_flow(self):
        active_role = self.get_active_role()
        active_role.act()
        self.game.turns += 1

    def get_active_role(self):
        if self.game.turns % 2 is 0:
            active_role = self.game.player
        else:
            active_role = self.game.wumpus
        return active_role


class ImplementedFlow(ProcedureFlow, TurnFlow):
    pass


class Game:
    def __init__(self, map, player, wumpus):
        self.map = None
        self.player = player
        self.wumpus = wumpus

        self.turns = 0


class Creature:
    __metaclass__ = ABCMeta

    @abstractmethod
    def act(self):
        pass


class Wumpus(Creature):
    def act(self):
        pass


class Player(Creature):
    def act(self):
        pass


def main():
    player = Player()
    wumpus = Wumpus()
    game = Game(None, wumpus, player)
    flow = ImplementedFlow(game)
    flow.procedure_flow()

if __name__ == '__main__':
    main()