import copy


def check_lose(board):
    for x in board[2]:
        if x != 'wall' and x != 0:
            return True
    return False


def del_line_if_need(pole):
    new_board = copy.deepcopy(pole.board)
    num = 0
    for y in range(pole.heig - 1, -1, -1):
        a = 0
        for x in range(pole.wid):
            if pole.board[y][x] == 'stone':
                a += 1
        if a == 10:
            del new_board[y]
            new_board = [['wall', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'wall']] + new_board
            num += 1
    return new_board, new_board != pole.board, num
