import pygame

#from figurs import gl_cell_size
from figurs import gl_cell_size


class Board:
    def __init__(self, screen):
        self.wid = 10
        self.heig = 13
        self.board = [[0] * self.wid for _ in range(self.heig)]
        self.screen = screen

        self.left = 10
        self.top = 10
        self.cell_size = gl_cell_size

    def render(self):
        for x in range(self.wid):
            for y in range(self.heig):
                pygame.draw.rect(self.screen, (100, 100, 100),
                                 (self.left + x * self.cell_size, self.top + y * self.cell_size,
                                  self.cell_size, self.cell_size), 1)
