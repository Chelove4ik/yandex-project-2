import copy

from clear import step_clear
from figurs import *
from check_collision import check_collision


class NowFig:

    def __init__(self, fig, screen, napr, pole):
        self.fig = fig
        self.screen = screen
        self.napr = napr
        self.pole = pole

        self.x = 4
        self.y = 0
        self.old_x = self.x
        self.old_y = self.y
        self.last_pole_board = copy.deepcopy(self.pole.board)

    def move(self, x, y):
        self.old_x = self.x
        self.old_y = self.y
        self.x = x
        self.y = y

    def edit_napr(self, napr):
        self.napr = napr

    def write_fig(self, pol=None):
        self.pole = step_clear(self.pole)
        info = (self.pole if pol is None else pol, self.x, self.y, self.napr)

        if self.fig == 'I':
            I(*info)
        elif self.fig == 'J':
            J(*info)
        elif self.fig == 'L':
            L(*info)
        elif self.fig == 'O':
            O(*info)
        elif self.fig == 'S':
            S(*info)
        elif self.fig == 'T':
            T(*info)
        elif self.fig == 'Z':
            Z(*info)

        check_info = check_collision(self)
        if check_info[0] or check_info[1]:
            self.x = self.old_x
            self.y = self.old_y
            self.pole.board = copy.deepcopy(self.last_pole_board)
        else:
            self.last_pole_board = copy.deepcopy(self.pole.board)
        if check_info[1]:
            return True
        else:
            return False

