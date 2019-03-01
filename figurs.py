gl_cell_size = 45

color_list = {
    0: (100, 100, 100),
    'I': (0, 0, 255),  # blue
    'J': (72, 61, 139),  # DARKSLATEBLUE
    'L': (255, 165, 0),  # orange
    'O': (255, 255, 0),  # yellow
    'S': (0, 255, 0),  # green
    'T': (160, 32, 240),  # purple
    'Z': (255, 0, 0),  # red
    'stone': (139, 141, 122)
}


def I(pole, x, y, napr):
    if napr == 0:
        pole.board[y][x + 1] = 'I'
        pole.board[y][x + 2] = 'I'
        pole.board[y][x + 3] = 'I'
        pole.board[y][x + 4] = 'I'
    elif napr == 1:
        pole.board[y - 1][x + 1] = 'I'
        pole.board[y][x + 1] = 'I'
        pole.board[y + 1][x + 1] = 'I'
        pole.board[y + 2][x + 1] = 'I'
    elif napr == 2:
        pole.board[y][x + 2] = 'I'
        pole.board[y][x + 1] = 'I'
        pole.board[y][x] = 'I'
        pole.board[y][x - 1] = 'I'
    elif napr == 3:
        pole.board[y + 1][x + 1] = 'I'
        pole.board[y][x + 1] = 'I'
        pole.board[y - 1][x + 1] = 'I'
        pole.board[y - 2][x + 1] = 'I'


def J(pole, x, y, napr):
    pole.board[y + 1][x + 1] = 'J'  # У всех J
    if napr == 0:
        pole.board[y][x + 1] = 'J'
        pole.board[y + 2][x + 1] = 'J'
        pole.board[y + 2][x] = 'J'
    elif napr == 1:
        pole.board[y][x] = 'J'
        pole.board[y + 1][x] = 'J'
        pole.board[y + 1][x + 2] = 'J'
    elif napr == 2:
        pole.board[y][x + 1] = 'J'
        pole.board[y][x + 2] = 'J'
        pole.board[y + 2][x + 1] = 'J'
    elif napr == 3:
        pole.board[y + 1][x] = 'J'
        pole.board[y + 1][x + 2] = 'J'
        pole.board[y + 2][x + 2] = 'J'


def L(pole, x, y, napr):
    pole.board[y + 1][x + 1] = 'L'  # У всех L
    if napr == 0:
        pole.board[y][x + 1] = 'L'
        pole.board[y + 2][x + 1] = 'L'
        pole.board[y + 2][x + 2] = 'L'
    elif napr == 1:
        pole.board[y + 1][x] = 'L'
        pole.board[y + 2][x] = 'L'
        pole.board[y + 1][x + 2] = 'L'
    elif napr == 2:
        pole.board[y][x] = 'L'
        pole.board[y][x + 1] = 'L'
        pole.board[y + 2][x + 1] = 'L'
    elif napr == 3:
        pole.board[y][x + 2] = 'L'
        pole.board[y + 1][x] = 'L'
        pole.board[y + 1][x + 2] = 'L'


def O(pole, x, y, napr=None):
    pole.board[y][x] = 'O'
    pole.board[y + 1][x] = 'O'
    pole.board[y][x + 1] = 'O'
    pole.board[y + 1][x + 1] = 'O'


def S(pole, x, y, napr):
    pole.board[y + 1][x + 1] = 'S'  # У всех S
    if napr == 0:
        pole.board[y][x + 1] = 'S'
        pole.board[y + 1][x + 2] = 'S'
        pole.board[y + 2][x + 2] = 'S'
    elif napr == 1:
        pole.board[y + 2][x] = 'S'
        pole.board[y + 2][x + 1] = 'S'
        pole.board[y + 1][x + 2] = 'S'
    elif napr == 2:
        pole.board[y][x] = 'S'
        pole.board[y + 1][x] = 'S'
        pole.board[y + 2][x + 1] = 'S'
    elif napr == 3:
        pole.board[y + 1][x] = 'S'
        pole.board[y][x + 1] = 'S'
        pole.board[y][x + 2] = 'S'


def T(pole, x, y, napr):
    pole.board[y + 1][x + 1] = 'T'  # У всех T
    if napr == 0:
        pole.board[y + 1][x] = 'T'
        pole.board[y][x + 1] = 'T'
        pole.board[y + 1][x + 2] = 'T'
    elif napr == 1:
        pole.board[y][x + 1] = 'T'
        pole.board[y + 1][x + 2] = 'T'
        pole.board[y + 2][x + 1] = 'T'
    elif napr == 2:
        pole.board[y + 1][x] = 'T'
        pole.board[y + 1][x + 2] = 'T'
        pole.board[y + 2][x + 1] = 'T'
    elif napr == 3:
        pole.board[y + 1][x] = 'T'
        pole.board[y][x + 1] = 'T'
        pole.board[y + 2][x + 1] = 'T'


def Z(pole, x, y, napr):
    pole.board[y + 1][x + 1] = 'Z'  # У всех Z
    if napr == 0:
        pole.board[y][x] = 'Z'
        pole.board[y][x+1] = 'Z'
        pole.board[y+1][x+2] = 'Z'
    elif napr == 1:
        pole.board[y][x+2] = 'Z'
        pole.board[y+1][x+2] = 'Z'
        pole.board[y+2][x+1] = 'Z'
    elif napr == 2:
        pole.board[y+1][x] = 'Z'
        pole.board[y+2][x+1] = 'Z'
        pole.board[y+2][x+2] = 'Z'
    elif napr == 3:
        pole.board[y+2][x] = 'Z'
        pole.board[y+1][x] = 'Z'
        pole.board[y][x+1] = 'Z'
