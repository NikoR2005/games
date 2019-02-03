import pygame.font
import pygame as pg
from turtle import *
from pygame.locals import *
import time

CAPTION = "Tetris"
SCREEN_SIZE = (1200, 1000)
SQUARE_SIZE = 80
BOX_COORDS = (740, 40)
BOX_HEIGHT = 20
BOX_WIDTH = 8

score = 0

YELLOW = pg.Color("yellow")
RED = pg.Color("red")
BLUE = pg.Color("blue")
BLACK = pg.Color("black")
clock = pg.time.Clock()
pg.font.init()
myfont = pg.font.SysFont('maison Sans MS', 30)


cube = [[[0, 0], [0, 1], [1, 0], [1, 1]],
       [[0, 0], [0, 1], [1, 0], [1, 1]],
       [[0, 0], [0, 1], [1, 0], [1, 1]],
       [[0, 0], [0, 1], [1, 0], [1, 1]]]

line = [[[0, 0], [0, 1], [0, 2]],
        [[0, 0], [1, 0], [2, 0]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 2], [1, 2], [2, 2]]]
pyramide = [[[0, 0], [0, 1], [0, 2], [1, 1]],
            [[0, 0], [1, 0], [2, 0], [1, 1]],
            [[2, 0], [2, 1], [2, 2], [1, 1]],
            [[0, 2], [1, 2], [2, 2], [1, 1]]]
angle = [[[0, 0], [0, 1], [0, 2], [1, 0]],
         [[0, 0], [1, 0], [2, 0], [2, 1]],
         [[2, 2], [2, 1], [2, 0], [1, 2]],
         [[0, 1], [0, 2], [2, 2], [1, 2]]]

shapes = [cube, line, pyramide, angle]


class Square(object):

    def __init__(self, x, y, size, color = RED):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.rect = pg.rect.Rect((self.x, self.y, self.size, self.size))

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)


class Circle(object):
    def __init__(self, circleColor, x, y, rad, thickness):
        self.x = x
        self.y = y
        self.rad = rad
        self.circleColor = circleColor
        self.thickness = thickness

    def drawcircle(self, screen):
        pg.draw.circle(screen, RED, (self.x, self.y), self.rad, self.thickness)


class Shape(object):
    def __init__(self, x, y, square_size, states, fill_color, background_color):
        self.states = states
        self.select_color = fill_color
        self.delete_color = background_color
        self.index = 0
        self.state = states[self.index]
        self.x = x
        self.y = y
        self.square_size = square_size

    def rotate(self, screen):
        if self.index == 3:
            self.index = 0
        else:
            self.index = self.index + 1
        self.state = self.states[self.index]

    def can_move(self, fix_states):
        return True

    def fall(self, fix_states):
        if self.can_move(fix_states):
            for cell in self.state:
                cell[1] = cell[1] + 1

    def draw(self, screen, remove):
        current_color = self.select_color
        if remove:
            current_color = self.delete_color
        for coordinates in self.state:
            x, y = self.x + coordinates[0] * self.square_size, self.y + coordinates[1] * self.square_size
            rect = Square(x, y, self.square_size, current_color)
            rect.draw(screen)


def text_to_screen(screen, text, x, y, size=50, color=(2, 2, 25)):
    try:

        text = str(text)
        text = myfont.render(text, True, color)
        screen.blit(text, (x, y))
    except:
        print('Font Error, saw it coming')


def draw_screen_not_used(screen):

    circle1 = Circle(RED, 65, 200, 10, 10)
    circle2 = Circle(RED, 65, 520, 10, 10)
    circle3 = Circle(RED, 305, 200, 10, 10)
    circle4 = Circle(RED, 305, 520, 10, 10)
    pg.draw.line(screen, (0, 0, 255), (0, 40), (1200, 40))
    pg.draw.line(screen, (0, 0, 255), (0, 0), (1200, 0))
    pg.draw.line(screen, (255, 0, 255), (740, 40), (740, 1000))
    pg.draw.line(screen, (255, 0, 255), (1060, 40), (1060, 1000))
    pg.draw.line(screen, (0, 0, 255), (600, 0), (600, 1000))
    pg.draw.line(screen, (0, 0, 255), (600, 0), (600, 1000))

    circle1.drawcircle(screen)
    circle2.drawcircle(screen)
    circle3.drawcircle(screen)
    circle4.drawcircle(screen)
    return [circle1, circle2, circle3, circle4]


def draw_shapes(screen):
    cube_shape = Shape(80, 80, SQUARE_SIZE, cube, RED, BLACK)
    cube_shape.draw(screen, False)
    pyramide_shape = Shape(80, 400, SQUARE_SIZE, pyramide, YELLOW, BLACK)
    pyramide_shape.draw(screen, False)
    angle_shape = Shape(320, 400, SQUARE_SIZE, angle, BLUE, BLACK)
    angle_shape.draw(screen, False)
    line_shape = Shape(320, 80, SQUARE_SIZE, line, YELLOW, BLACK)
    line_shape.draw(screen, False)
    return [cube_shape, pyramide_shape, angle_shape, line_shape]


def main():
    running = True
    pg.init()
    pg.display.set_caption(CAPTION)
    pg.display.set_mode(SCREEN_SIZE)
    pg.font.init()
    basicfont = pygame.font.SysFont(None, 60)
    text = basicfont.render('         Choose your forms.                     Press SPACE start.', True, (55, 0, 0), (0, 255, 255))

    textrect = text.get_rect()
    screen = pg.display.get_surface()

    grid = []
    for k in range(BOX_HEIGHT):
        row = []
        for i in range(BOX_WIDTH):
            cell = (BOX_COORDS[0] + i * BOX_COORDS[1], BOX_COORDS[1] + k * SQUARE_SIZE, RED, (k, i))
            row.append(cell)
        grid.append(row)

    fix_states = []v
    circles = draw_screen_not_used(screen)
    shapes = draw_shapes(screen)

    while running:
        for cell in grid:
            sq = Square(cell[0], cell[1], SQUARE_SIZE)
            sq.draw(screen)
        keys = pygame.key.get_pressed()
        if keys[K_SPACE]:
            for shape in shapes:
                shape.draw(screen, True)
                shape.rotate(screen)
                shape.draw(screen, False)

        next_states = []
        for state in cube[0]:
            state = [state[0] + 1, state[1]]
            next_states.append(state)

        if state[0] == 15:
            fix_states.extend(cube[0])

        evt = pygame.event.get()
        for event in evt:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                for circle in circles:
                    if circle.x - circle.rad < pos[0] and pos[0] < circle.x + circle.rad and circle.y - circle.rad < pos[1] and pos[1] < circle.y + circle.rad:
                        pg.draw.circle(screen, YELLOW, (circle.x, circle.y), circle.rad, circle.thickness)
                        if circle.thickness == 10:
                            circle.thickness = 2
                        else:
                            circle.thickness = 10
                        circle.drawcircle(screen)

        pg.display.update()
        clock.tick(10)


if __name__ == "__main__":
    main()
