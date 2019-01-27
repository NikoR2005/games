import os
import sys
import time
import pygame.font
import pygame as pg
from turtle import *
from pygame.locals import *
from tkinter import *

CAPTION = "Tetris"
SCREEN_SIZE = (1200, 1000)
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

line = [[[0, 0], [0, 1], [0, 2], [1, 2]],
       [[0, 0], [0, 1], [0, 2], [1, 2]],
       [[0, 0], [0, 1], [0, 2], [1, 2]],
       [[0, 0], [0, 1], [0, 2], [1, 2]]]
pyramide = [[[0, 0], [0, 1], [0, 2], [1, 1]],
       [[0, 0], [1, 0], [2, 0], [1, 1]],
       [[0, 1], [1, 0], [1, 1], [1, 2]],
       [[0, 0], [0, 1], [0, 2], [1, 2]]]
angle = [[[0, 0], [0, 1], [0, 2], [1, 0]],
             [[0, 0], [1, 0], [2, 0], [2, 1]],
             [[1, 0], [1, 1], [1, 2], [2, 0]],
             [[0, 0], [0, 1], [0, 2], [1, 2]]]

shapes = [cube, line, pyramide, angle]


class Rectangle(object):

    def __init__(self, x, y, width, height, color = RED):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pg.rect.Rect((self.x, self.y, self.width, self.height))

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
    def __init__(self, states, select_color):
        self.states = states
        self.color = select_color

        self.state = states[0]


    def rotate(self):
        pass

    def can_move(self,  fix_states):
        pass

    def fall(self):
        return self.state

    def draw(self, init_x, init_y, square_size, screen):
        for coordinates in self.state:
            rect = Rectangle(init_x + coordinates[0] * square_size, init_y + coordinates[1] * square_size, square_size, square_size, self.color)
            rect.draw(screen)

def text_to_screen(screen, text, x, y, size=50, color=(2, 2, 25)):
    try:

        text = str(text)
        text = myfont.render(text, True, color)
        screen.blit(text, (x, y))

    except:
        print('Font Error, saw it coming')

def draw_screen_not_used(screen):
    cube_shape = Shape(cube, RED)
    cube_shape.draw(80, 80, 80, screen)
    line_shape = Shape(line, YELLOW)
    line_shape.draw(80, 240, 80, screen)
    form2_1 = Rectangle(320, 80, 80, 80)
    form2_2 = Rectangle(320, 160, 80, 80)
    form2_3 = Rectangle(320, 240, 80, 80)
    form2_4 = Rectangle(400, 240, 80, 80)
    form3_1 = Rectangle(80, 480, 80, 80)
    form3_2 = Rectangle(160, 480, 80, 80)
    form3_3 = Rectangle(80, 400, 80, 80)
    form3_4 = Rectangle(80, 560, 80, 80)
    form4_1 = Rectangle(320, 400, 80, 80)
    form4_2 = Rectangle(400, 400, 80, 80)
    form4_3 = Rectangle(320, 480, 80, 80)
    form4_4 = Rectangle(400, 480, 80, 80)
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
    form2_1.draw(screen)
    form2_2.draw(screen)
    form2_3.draw(screen)
    form2_4.draw(screen)
    form3_1.draw(screen)
    form3_2.draw(screen)
    form3_3.draw(screen)
    form3_4.draw(screen)
    form4_1.draw(screen)
    form4_2.draw(screen)
    form4_3.draw(screen)
    form4_4.draw(screen)
    circle1.drawcircle(screen)
    circle2.drawcircle(screen)
    circle3.drawcircle(screen)
    circle4.drawcircle(screen)
    return [circle1, circle2, circle3, circle4]

def main():
    running = True
    pg.init()
    pg.display.set_caption(CAPTION)
    dsp = pg.display.set_mode(SCREEN_SIZE)
    pg.font.init()
    basicfont = pygame.font.SysFont(None, 60)
    text = basicfont.render('         Choose your forms.                     Press SPACE start.', True, (55, 0, 0), (0, 255, 255))

    textrect = text.get_rect()
    screen = pg.display.get_surface()


    grid = []
    for k in range(20):
        row = []
        for i in range(8):
            cell = (740 + i * 40, 40 + k * 40, RED, (k, i))
            row.append(cell)
        grid.append(row)

    fix_states = []


    circles = draw_screen_not_used(screen)
    while running:
        shape = Shape(cube[0], RED)
        state = shape.fall()
        for row in grid:
            for cell in row:
                if cell[3] in cube or cell[3] in fix_states:
                    rect = Rectangle(cell[0], cell[1], 40, 40, YELLOW)
                else:
                    rect = Rectangle(cell[0], cell[1], 40, 40, cell[2])
                rect.draw(screen)

        next_states = []
        for state in cube[0]:
            state = [state[0] + 1, state[1]]
            next_states.append(state)

        if state[0] == 15:
            fix_states.extend(cube[0])

        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for circle in circles:
                    if circle.x - circle.rad < pos[0] and pos[0] < circle.x + \
                            circle.rad and circle.y - circle.rad < pos[1] and pos[1] < circle.y + circle.rad:
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
