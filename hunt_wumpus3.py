# -*- coding: utf8 -*-
import os
from abc import ABCMeta, abstractmethod
from wumpus_Game import *
from wumpus_Creature import *
from wumpus_Arena import *


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
        role_act_flow()
        self.game.turns += 1
        """

    @abstractmethod
    def role_act_flow(self):
        """
        (player_act_flow() if (self.game.turns % 2 == 0) else
         wumpus_act_flow())
         """

    @abstractmethod
    def player_act_flow(self):
        """
        player.get_action()
        (self.game.attack(player, wumpus) if (player.is_attack_action()) else
         self.game.player_move())
        """

    @abstractmethod
    def wumpus_act_flow(self):
        """
        self.game.wumpus_move()
        """


class ProcedureFlow(Flow):
    def procedure_flow(self):
        while self.is_game_over() is False:
            self.turn_flow()
        self.display_score()

    def is_game_over(self):
        return (True if (self.game.wumpus is None or
                         self.game.player is None)else
                False)

    def display_score(self):
        print "Player:   " + str(self.game.player)
        print "Wumpus:   " + str(self.game.wumpus)
        print "Turns :   " + str(self.game.turns)


class TurnFlow(Flow):
    def turn_flow(self):
        self.role_act_flow()
        self.game.turns += 1


class RoleActFlow(Flow):
    def role_act_flow(self):
        (self.player_act_flow() if (self.game.turns % 2 == 0) else
         self.wumpus_act_flow())


class PlayerActFlow(Flow):
    def player_act_flow(self):
        self.game.player.get_action()
        (self.game.attack(self.game.player, self.game.wumpus) if
                         (self.game.player.is_attack_action()) else
         self.game.move(self.game.player))


class WumpusActFlow(Flow):
    def wumpus_act_flow(self):
        self.game.move(self.game.wumpus)
        #os.system("cls")
        for i in self.game.arena.array:
                print i


class ImplementedFlow(ProcedureFlow, TurnFlow, RoleActFlow,
                      PlayerActFlow, WumpusActFlow):
    pass


def main():
    player = Player()
    wumpus = Wumpus()
    x_limit = 5
    y_limit = 5
    arena = Arena(x_limit, y_limit)
    game = Game(arena, player, wumpus)

    flow = ImplementedFlow(game)
    flow.procedure_flow()


if __name__ == '__main__':
    main()
