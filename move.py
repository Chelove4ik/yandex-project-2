from figurs import *


class NowFig:
    def __init__(self, fig, screen, napr):
        self.fig = fig
        self.screen = screen
        self.napr = napr

        self.x = 190
        self.y = 10

    def collision(self):
        pass

    def edit_napr(self, napr):
        self.napr = napr

    def render(self):
        info = (self.screen, self.x, self.y, self.napr)
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
