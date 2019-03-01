def check_collision(self):
    num_stone1 = 0
    num_stone2 = 0
    num_wall1 = 0
    num_wall2 = 0

    for y in range(self.pole.heig + 1):
        for x in range(self.pole.wid):
            if self.pole.board[y][x] == 'wall':
                num_wall1 += 1
            if self.pole.board[y][x] == 'stone':
                num_stone1 += 1
            if self.last_pole_board[y][x] == 'wall':
                num_wall2 += 1
            if self.last_pole_board[y][x] == 'stone':
                num_stone2 += 1

    return num_wall1 != num_wall2, num_stone1 != num_stone2
