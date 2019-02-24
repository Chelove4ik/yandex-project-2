import pygame

gl_cell_size = 45

color_list = {
    'I': pygame.Color('blue'),
    'J': pygame.Color('DARKSLATEBLUE'),
    'L': pygame.Color('orange'),
    'O': pygame.Color('yellow'),
    'S': pygame.Color('green'),
    'T': pygame.Color('purple'),
    'Z': pygame.Color('red')
}


def I(screen, x, y, napr):
    pygame.draw.rect(screen, color_list['I'], (x, y, gl_cell_size if napr == 1 or napr == 3 else gl_cell_size * 4,
                                               gl_cell_size if napr == 0 or napr == 2 else gl_cell_size * 4))


def J(screen, x, y, napr):
    if napr == 0:
        lst = [
            (x + gl_cell_size, y),
            (x + gl_cell_size * 2, y),
            (x + gl_cell_size * 2, y + gl_cell_size * 3),
            (x, y + gl_cell_size * 3),
            (x, y + gl_cell_size * 2),
            (x + gl_cell_size, y + gl_cell_size * 2),
        ]
    elif napr == 1:
        lst = [
            (x, y),
            (x + gl_cell_size, y),
            (x + gl_cell_size, y + gl_cell_size),
            (x + gl_cell_size * 3, y + gl_cell_size),
            (x + gl_cell_size * 3, y + gl_cell_size * 2),
            (x, y + gl_cell_size * 2),
        ]
    elif napr == 2:
        lst = [
            (x + gl_cell_size, y),
            (x + gl_cell_size * 3, y),
            (x + gl_cell_size * 3, y + gl_cell_size),
            (x + gl_cell_size * 2, y + gl_cell_size),
            (x + gl_cell_size * 2, y + gl_cell_size * 3),
            (x + gl_cell_size, y + gl_cell_size * 3),
        ]
    elif napr == 3:
        lst = [
            (x, y + gl_cell_size),
            (x + gl_cell_size * 3, y + gl_cell_size),
            (x + gl_cell_size * 3, y + gl_cell_size * 3),
            (x + gl_cell_size * 2, y + gl_cell_size * 3),
            (x + gl_cell_size * 2, y + gl_cell_size * 2),
            (x, y + gl_cell_size * 2),
        ]
    pygame.draw.polygon(screen, color_list['J'], lst)


def L(screen, x, y, napr):
    if napr == 0:
        lst = [
            (x + gl_cell_size, y),
            (x + gl_cell_size * 2, y),
            (x + gl_cell_size * 2, y + gl_cell_size * 2),
            (x + gl_cell_size * 3, y + gl_cell_size * 2),
            (x + gl_cell_size * 3, y + gl_cell_size * 3),
            (x + gl_cell_size, y + gl_cell_size * 3),
        ]
    elif napr == 1:
        lst = [
            (x, y + gl_cell_size),
            (x + gl_cell_size * 3, y + gl_cell_size),
            (x + gl_cell_size * 3, y + gl_cell_size * 2),
            (x + gl_cell_size, y + gl_cell_size * 2),
            (x + gl_cell_size, y + gl_cell_size * 3),
            (x, y + gl_cell_size * 3),
        ]
    elif napr == 2:
        lst = [
            (x, y),
            (x + gl_cell_size * 2, y),
            (x + gl_cell_size * 2, y + gl_cell_size * 3),
            (x + gl_cell_size, y + gl_cell_size * 3),
            (x + gl_cell_size, y + gl_cell_size),
            (x, y + gl_cell_size),
        ]
    elif napr == 3:
        lst = [
            (x, y + gl_cell_size),
            (x + gl_cell_size * 2, y + gl_cell_size),
            (x + gl_cell_size * 2, y),
            (x + gl_cell_size * 3, y),
            (x + gl_cell_size * 3, y + gl_cell_size * 2),
            (x, y + gl_cell_size * 2),
        ]
    pygame.draw.polygon(screen, color_list['L'], lst)


def O(screen, x, y, napr=None):
    pygame.draw.rect(screen, color_list['O'], (x, y, gl_cell_size * 2, gl_cell_size * 2))


def S(screen, x, y, napr):
    if napr == 0 or napr == 2:
        lst = [
            (x, y + gl_cell_size),
            (x + gl_cell_size, y + gl_cell_size),
            (x + gl_cell_size, y),
            (x + gl_cell_size * 3, y),
            (x + gl_cell_size * 3, y + gl_cell_size),
            (x + gl_cell_size * 2, y + gl_cell_size),
            (x + gl_cell_size * 2, y + gl_cell_size * 2),
            (x, y + gl_cell_size * 2),
        ]
    elif napr == 1 or napr == 3:
        lst = [
            (x, y),
            (x + gl_cell_size, y),
            (x + gl_cell_size, y + gl_cell_size),
            (x + gl_cell_size * 2, y + gl_cell_size),
            (x + gl_cell_size * 2, y + gl_cell_size * 3),
            (x + gl_cell_size, y + gl_cell_size * 3),
            (x + gl_cell_size, y + gl_cell_size * 2),
            (x, y + gl_cell_size * 2),
        ]

    pygame.draw.polygon(screen, color_list['S'], lst)


def T(screen, x, y, napr):
    if napr == 0:
        lst = [
            (x, y + gl_cell_size),
            (x + gl_cell_size, y + gl_cell_size),
            (x + gl_cell_size, y),
            (x + gl_cell_size * 2, y),
            (x + gl_cell_size * 2, y + gl_cell_size),
            (x + gl_cell_size * 3, y + gl_cell_size),
            (x + gl_cell_size * 3, y + gl_cell_size * 2),
            (x, y + gl_cell_size * 2),
        ]
    elif napr == 1:
        lst = [
            (x + gl_cell_size, y),
            (x + gl_cell_size * 2, y),
            (x + gl_cell_size * 2, y + gl_cell_size),
            (x + gl_cell_size * 3, y + gl_cell_size),
            (x + gl_cell_size * 3, y + gl_cell_size * 2),
            (x + gl_cell_size * 2, y + gl_cell_size * 2),
            (x + gl_cell_size * 2, y + gl_cell_size * 3),
            (x + gl_cell_size, y + gl_cell_size * 3),
        ]
    elif napr == 2:
        lst = [
            (x, y + gl_cell_size),
            (x + gl_cell_size * 3, y + gl_cell_size),
            (x + gl_cell_size * 3, y + gl_cell_size * 2),
            (x + gl_cell_size * 2, y + gl_cell_size * 2),
            (x + gl_cell_size * 2, y + gl_cell_size * 3),
            (x + gl_cell_size, y + gl_cell_size * 3),
            (x + gl_cell_size, y + gl_cell_size * 2),
            (x, y + gl_cell_size * 2),
        ]
    elif napr == 3:
        lst = [
            (x, y + gl_cell_size),
            (x + gl_cell_size, y + gl_cell_size),
            (x + gl_cell_size, y),
            (x + gl_cell_size * 2, y),
            (x + gl_cell_size * 2, y + gl_cell_size * 3),
            (x + gl_cell_size, y + gl_cell_size * 3),
            (x + gl_cell_size, y + gl_cell_size * 2),
            (x, y + gl_cell_size * 2),
        ]
    pygame.draw.polygon(screen, color_list['T'], lst)


def Z(screen, x, y, napr):
    if napr == 0 or napr == 2:
        lst = [
            (x, y),
            (x + gl_cell_size * 2, y),
            (x + gl_cell_size * 2, y + gl_cell_size),
            (x + gl_cell_size * 3, y + gl_cell_size),
            (x + gl_cell_size * 3, y + gl_cell_size * 2),
            (x + gl_cell_size, y + gl_cell_size * 2),
            (x + gl_cell_size, y + gl_cell_size),
            (x, y + gl_cell_size),
        ]
    elif napr == 1 or napr == 3:
        lst = [
            (x + gl_cell_size, y + gl_cell_size),
            (x + gl_cell_size*2, y + gl_cell_size),
            (x + gl_cell_size*2, y),
            (x + gl_cell_size*3, y),
            (x + gl_cell_size*3, y + gl_cell_size*2),
            (x + gl_cell_size*2, y + gl_cell_size*2),
            (x + gl_cell_size*2, y + gl_cell_size*3),
            (x + gl_cell_size, y + gl_cell_size*3),
        ]
    pygame.draw.polygon(screen, color_list['Z'], lst)
