import pygame

from random import choice

running = True
pygame.init()

size = width, height = 800, 605
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))

clock = pygame.time.Clock()
fps = 30

figurs = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']

color_list = {
    'I': pygame.Color('blue'),
    'J': pygame.Color('DARKSLATEBLUE'),
    'L': pygame.Color('orange'),
    'O': pygame.Color('yellow'),
    'S': pygame.Color('green'),
    'T': pygame.Color('purple'),
    'Z': pygame.Color('red')
}

points_list = {
    'I': '4',
    'J': '6',
    'L': '6',
    'O': '4',
    'S': '8',
    'T': '8',
    'Z': '8',
}


class Board:
    def __init__(self):
        self.wid = 10
        self.heig = 13
        self.board = [[0] * self.wid for _ in range(self.heig)]

        self.left = 10
        self.top = 10
        self.cell_size = 45

    def render(self):
        for x in range(self.wid):
            for y in range(self.heig):
                pygame.draw.rect(screen, (255, 255, 255),
                                 (self.left + x * self.cell_size, self.top + y * self.cell_size,
                                  self.cell_size, self.cell_size), 1)


class Menu:
    def __init__(self):
        pass

    def render(self):
        rend_fig(choice(figurs))


def rend_fig(fig, coord, vect):
    coords_list = []
    for i in points_list[fig]:
        if vect == '0':
            coords_list.append(())


    if len(args) == 4:
        pygame.draw.polygon(screen, color_list[fig])

pole = Board()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pole.render()

    pygame.display.flip()
    clock.tick(fps)
