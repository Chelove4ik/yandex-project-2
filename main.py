import pygame

from random import choice

from pygame.constants import K_LEFT, K_RIGHT, K_UP, K_DOWN

from figurs import gl_cell_size
from time import clock
from board_file import Board
from move import NowFig

running = True
pygame.init()

size = width, height = 800, 605
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))

clck = pygame.time.Clock()
fps = 30

figurs = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']

points_list = {
    'I': 4,
    'J': 6,
    'L': 6,
    'O': 4,
    'S': 8,
    'T': 8,
    'Z': 8,
}

next_fig = choice(figurs)
napr = 0


class Menu:
    def __init__(self):
        pass

    def render(self):
        pass


a = clock()
time_for_press = clock()

pole = Board(screen)
now_fig = NowFig(next_fig, screen, napr)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_UP:
                napr = (napr + 1) % 4
            elif event.key == pygame.K_RIGHT:
                pass
            elif event.key == pygame.K_DOWN:
                pass
            time_for_press = clock()

    pressed = pygame.key.get_pressed()
    if clock() - time_for_press > 0.3:
        if pressed[K_LEFT]:
            pass
        if pressed[K_RIGHT]:
            pass
        if pressed[K_UP]:
            napr = (napr + 1) % 4
        if pressed[K_DOWN]:
            pass
        time_for_press = clock()

    screen.fill((0, 0, 0))
    pole.render()
    # if clock() - a > 1:
    #    coords[y] -= gl_cell_size

    now_fig.edit_napr(napr)
    now_fig.render()

    pygame.display.flip()
    clck.tick(fps + 20)
