import pygame

from random import choice

from pygame.constants import K_LEFT, K_RIGHT, K_UP, K_DOWN

from figurs import gl_cell_size
from time import clock
from board_file import Board
from move import NowFig
from checkers import *


def main_fun():
    running = True
    pygame.init()
    pygame.font.init()

    myfont = pygame.font.SysFont('Comic Sans MS', 40)

    pause_text = myfont.render('Pause', False, (255, 255, 255))
    esc = True
    count = 0

    size = 750, 605
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))

    clck = pygame.time.Clock()
    fps = 24

    figurs = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']

    napr = 0

    time_down = clock()
    time_for_press = clock()

    pole = Board(screen)
    now_fig = NowFig(choice(figurs), screen, napr, pole)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not esc:
                    now_fig.move(now_fig.x - 1, now_fig.y)
                elif event.key == pygame.K_UP and not esc:
                    napr = (napr + 1) % 4
                elif event.key == pygame.K_RIGHT and not esc:
                    now_fig.move(now_fig.x + 1, now_fig.y)
                elif event.key == pygame.K_DOWN and not esc:
                    now_fig.move(now_fig.x, now_fig.y + 1)
                elif event.key == pygame.K_ESCAPE:
                    esc = not esc
                time_for_press = clock()

        if esc:
            screen.blit(pause_text, (300, 250))
            pygame.display.flip()
            continue

        pressed = pygame.key.get_pressed()
        if clock() - time_for_press > 0.2:
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
        now_fig.edit_napr(napr)
        pole.render()

        if clock() - time_down >= 1:
            now_fig.move(now_fig.x, now_fig.y + 1)
            time_down = clock()

        if now_fig.write_fig():

            for x in range(pole.wid):
                for y in range(pole.heig):
                    if pole.board[y][x] != 'stone' and pole.board[y][x] != 'wall' and pole.board[y][x] != 0:
                        pole.board[y][x] = 'stone'

            if check_lose(now_fig.pole.board):
                screen.fill((0, 0, 0))
                text = myfont.render('Ваш счёт = {}'.format(count), False, (255, 255, 255))
                screen.blit(text, (200, 200))

                text = myfont.render('Чтобы начать заного нажмите spase', False, (255, 255, 255))
                screen.blit(text, (50, 300))

                a = True
                pygame.display.flip()
                while a:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit(0)
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                pole = Board(screen)
                                count = 0
                                a = False

            diff_pole = del_line_if_need(pole)
            pole.board = diff_pole[0]
            if diff_pole[1]:
                count += 100

            napr = 0
            now_fig = NowFig(choice(figurs), screen, napr, pole)

        count_text = myfont.render(str(count), False, (255, 255, 255))

        screen.blit(count_text, (530, 300))

        pygame.display.flip()
        clck.tick(fps)


if __name__ == '__main__':
    main_fun()
