def step_clear(pole):
    for x in range(pole.wid):
        for y in range(pole.heig):
            if pole.board[y][x] != 'stone' and pole.board[y][x] != 'wall':
                pole.board[y][x] = 0
    return pole
