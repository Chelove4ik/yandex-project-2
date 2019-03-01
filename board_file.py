import pygame

from figurs import gl_cell_size, color_list


class Board:
    def __init__(self, screen):
        self.wid = 12
        self.heig = 13
        self.board = [[0] * self.wid for _ in range(self.heig)]
        for i in range(self.heig):
            self.board[i][0] = 'wall'
            self.board[i][-1] = 'wall'
        self.board.append(['stone'] * self.wid)
        self.screen = screen

        self.left = 10 - gl_cell_size
        self.top = 10
        self.cell_size = gl_cell_size

    def render(self):
        for x in range(1, self.wid-1):
            for y in range(self.heig):
                pygame.draw.rect(self.screen, color_list[self.board[y][x]],
                                 (self.left + x * self.cell_size, self.top + y * self.cell_size,
                                  self.cell_size, self.cell_size), 1 if self.board[y][x] == 0 else 0)
