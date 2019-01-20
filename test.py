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

clock = pg.time.Clock()
pg.font.init()

myfont = pg.font.SysFont('Comic Sans MS', 30)


class Rectangle(object):

    def __init__(self, x, y, width, height, color=RED):
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


def text_to_screen(screen, text, x, y, size=50, color=(2, 2, 25)):
    try:

        text = str(text)
        text = myfont.render(text, True, color)
        screen.blit(text, (x, y))

    except:
        print('Font Error, saw it coming')


def draw_screen(screen):
    form1_1 = Rectangle(80, 80, 80, 80, RED)
    form1_2 = Rectangle(80, 160, 80, 80, YELLOW)
    form1_3 = Rectangle(80, 240, 80, 80)
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
    circle1 = Circle(RED, 65, 200, 10, 2)
    circle2 = Circle(RED, 65, 520, 10, 2)
    circle3 = Circle(RED, 305, 200, 10, 2)
    circle4 = Circle(RED, 305, 520, 10, 2)
    pg.draw.line(screen, (0, 0, 255), (0, 40), (1200, 40))
    pg.draw.line(screen, (0, 0, 255), (0, 0), (1200, 0))
    pg.draw.line(screen, (255, 0, 255), (740, 40), (740, 1000))
    pg.draw.line(screen, (255, 0, 255), (1060, 40), (1060, 1000))
    pg.draw.line(screen, (0, 0, 255), (600, 0), (600, 1000))
    pg.draw.line(screen, (0, 0, 255), (600, 0), (600, 1000))
    form1_1.draw(screen)
    form1_2.draw(screen)
    form1_3.draw(screen)
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
    pg.display.set_mode(SCREEN_SIZE)
    pg.font.init()
    basicfont = pygame.font.SysFont(None, 60)
    text = basicfont.render('         Choose your forms.                     Press SPACE start.', True, (55, 0, 0),
                            (0, 255, 255))
    textrect = text.get_rect()
    screen = pg.display.get_surface()


    grid = []
    for k in range(20):
        row = []
        for i in range(8):
            cell = (740 + i * 40, 40 + k * 40, RED, (k, i))
            row.append(cell)
        grid.append(row)
    print(grid)

    fall_states = [(0, 5), (0 + 1, 6), (0, 7), (0, 6)]
    fix_states = []

    circles = draw_screen(screen)
    while running:

        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for circle in circles:
                    if circle.x - circle.rad < pos[0] and pos[0] < circle.x + circle.rad and circle.y - circle.rad < pos[1] and pos[1] < circle.y + circle.rad:
                        if circle.thickness == 10:
                            circle.thickness = 2
                            circle.circleColor = BLUE
                            circle.drawcircle(screen)
                        else:
                            circle.thickness = 10
                            circle.circleColor = YELLOW
                            circle.drawcircle(screen)

        for row in grid:
            for cell in row:
                if cell[3] in fall_states or cell[3] in fix_states:
                    rect = Rectangle(cell[0], cell[1], 40, 40, YELLOW)
                else:
                    rect = Rectangle(cell[0], cell[1], 40, 40, cell[2])
                rect.draw(screen)

        next_states = []
        for state in fall_states:

            state = (state[0] + 1, state[1])
            next_states.append(state)


        fall_states = next_states
        if state[0] == 15:
            fix_states.extend(fall_states)
            print('ok')
        #    if state[0] == 15:
          #      state[0] = 0




        pg.display.update()
        clock.tick(10)

if __name__ == "__main__":
    main()
