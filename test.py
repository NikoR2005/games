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
BACKGROUND_COLOR = pg.Color("red")
YELLOW_COLOR = pg.Color("yellow")
red = (255, 0, 0)
rectangle1Color = (225, 0, 200)
rectangle2Color = (0, 50, 225)
rectangle3Color = (225, 225, 225)
rectangle4Color = (1, 1, 1)
rectangle5Color = (0, 225, 0)
rectangle6Color = (125, 125, 125)

clock = pg.time.Clock()
pg.font.init(),

myfont = pg.font.SysFont('Comic Sans MS', 30)


class Rectangle():

    def __init__(self, x, y, width, height, colour ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

        # self.rectangle1Color = rectangle1Color
        # self.rectangle2Color = rectangle2Color

        self.rect = pg.rect.Rect((self.x, self.y, self.width, self.height))

    def draw(self, screen):
        pg.draw.rect(screen, (0, 0, 255), self.rect)

    def draw1(self, screen):
        pg.draw.rect(screen, (0, 255, 0), self.rect)

    def draw2(self, screen):
        pg.draw.rect(screen, (255, 0, 0), self.rect)

    def draw3(self, screen):
        pg.draw.rect(screen, YELLOW_COLOR, self.rect)




def text_to_screen(screen, text, x, y, size=50, color=(225, 225, 225)):
    try:

        text = str(text)
        text = myfont.render(text, True, color)
        screen.blit(text, (x, y))

    except:
        print('Font Error, saw it coming')


class Circle(object):
    def __init__(self, circleColor, x, y, rad, thickness):
        self.x = x
        self.y = y
        self.rad = rad
        self.circleColor = circleColor
        self.thickness = thickness

    def drawcircle(self, screen):
        pg.draw.circle(screen, BACKGROUND_COLOR, (self.x, self.y), self.rad, self.thickness)


def main():
    running = True
    pg.init()

    pg.display.set_caption(CAPTION)
    pg.display.set_mode(SCREEN_SIZE)
    pg.font.init()
    form1_1 = Rectangle(80, 80, 80, 80)
    form1_2 = Rectangle(80, 160, 80, 80)
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
    form11 = Rectangle(780, 40, 40, 40)
    circle1 = Circle(BACKGROUND_COLOR, 65, 200, 10, 2)
    circle2 = Circle(BACKGROUND_COLOR, 65, 520, 10, 2)
    circle3 = Circle(BACKGROUND_COLOR, 305, 200, 10, 2)
    circle4 = Circle(BACKGROUND_COLOR, 305, 520, 10, 2)

    basicfont = pygame.font.SysFont(None, 60)
    text = basicfont.render('         Choose your forms.                     Press SPACE start.', True, (55, 0, 0),
                            (255, 255, 255))
    textrect = text.get_rect()
    screen = pg.display.get_surface()

    #create the grid for tetris shapes
    grid = []
    for k in range (12):
        row = []
        for i in range(8):
            cell = (740 + i * 40, 40 + k*40,red)
            row.append(cell)
        grid.append(row)
    print(grid)


    while running:
        screen.fill((255, 255, 255))
        screen.blit(text, textrect)

        pg.draw.line(screen, (0, 0, 255), (0, 40), (1200, 40))
        pg.draw.line(screen, (0, 0, 255), (0, 0), (1200, 0))
        pg.draw.line(screen, (255, 0, 255), (740, 40), (740, 1000))
        pg.draw.line(screen, (255, 0, 255), (1060, 40), (1060, 1000))
        pg.draw.line(screen, (0, 0, 255), (600, 0), (600, 1000))
        pg.draw.line(screen, (0, 0, 255), (600, 0), (600, 1000))
        pg.draw.line(screen, (0, 0, 150), (1020, 40), (1020, 1000))
        pg.draw.line(screen, (0, 0, 150), (980, 40), (980, 1000))
        pg.draw.line(screen, (0, 0, 150), (940, 40), (940, 1000))
        pg.draw.line(screen, (0, 0, 150), (900, 40), (900, 1000))
        pg.draw.line(screen, (0, 0, 150), (860, 40), (860, 1000))
        pg.draw.line(screen, (0, 0, 150), (820, 40), (820, 1000))
        pg.draw.line(screen, (0, 0, 150), (780, 40), (780, 1000))
        form1_1.draw(screen)
        form1_2.draw(screen)
        form1_3.draw(screen)
        form2_1.draw1(screen)
        form2_2.draw1(screen)
        form2_3.draw1(screen)
        form2_4.draw1(screen)
        form3_1.draw2(screen)
        form3_2.draw2(screen)
        form3_3.draw2(screen)
        form3_4.draw2(screen)
        form4_1.draw3(screen)
        form4_2.draw3(screen)
        form4_3.draw3(screen)
        form4_4.draw3(screen)
        circle1.drawcircle(screen)
        circle2.drawcircle(screen)
        circle3.drawcircle(screen)
        circle4.drawcircle(screen)
        form11.draw(screen)

        ev = pygame.event.get()

        for event in ev:

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if circle1.x - circle1.rad < pos[0] and pos[0] < circle1.x + circle1.rad \
                        and circle1.y - circle1.rad < pos[1] and pos[1] < circle1.y + circle1.rad:

                    if circle1.thickness == 10:
                        circle1.thickness = 2
                    else:
                        circle1.thickness = 10

                if circle2.x - circle2.rad < pos[0] and pos[0] < circle2.x + circle2.rad \
                        and circle2.y - circle2.rad < pos[1] and pos[1] < circle2.y + circle2.rad:

                    if circle2.thickness == 10:
                        circle2.thickness = 2
                    else:
                        circle2.thickness = 10

                if circle3.x - circle3.rad < pos[0] and pos[0] < circle3.x + circle3.rad \
                        and circle3.y - circle3.rad < pos[1] and pos[1] < circle3.y + circle3.rad:

                    if circle3.thickness == 10:
                        circle3.thickness = 2
                    else:
                        circle3.thickness = 10
                if circle4.x - circle4.rad < pos[0] and pos[0] < circle4.x + circle4.rad \
                        and circle4.y - circle4.rad < pos[1] and pos[1] < circle4.y + circle4.rad:

                    if circle4.thickness == 10:
                        circle4.thickness = 2
                    else:
                        circle4.thickness = 10
        for row in grid:
            for cell in row:
                rect = Rectangle(cell[0], cell[1], 40, 40)
                rect.draw1(screen)
#                pg.draw.rect(cell[0], cell[1], cell[2])
        pg.display.update()

        clock.tick(40)


if __name__ == "__main__":
    main()


