import os
import sys
import time
import pygame.font
import pygame as pg
from turtle import *
from pygame.locals import *


pygame.init()
CAPTION = "Tetris"
SCREEN_SIZE = (600, 800)
score = 0
BACKGROUND_COLOR = pg.Color("red")
red = (255, 0, 0)
rectangle1Color = (225, 0, 200 )
rectangle2Color = (0, 50, 225)
rectangle3Color = (225, 225, 225)
rectangle4Color = (1, 1, 1)
rectangle5Color = (0, 225, 0)
rectangle6Color = (125, 125, 125)

clock = pg.time.Clock()
pg.font.init(),

myfont = pg.font.SysFont('Comic Sans MS', 30)


class rectangle():

    def __init__(self ,x ,y):
        self.x = x
        self.y = y
        self.rect1_size = (40, 80)
        self.rect2_size = (80, 80)
        self.rect3_size = (40, 40)
        self.rect4_size = ()
        self.rect1 = pg.rect((self.x, self.y))


    def rectangle1(self, screen):
        pg.draw.rect1(screen, rectangle1Color, self.rect1)

def text_to_screen(screen, text, x, y, size = 50,
            color = (225, 225, 225)):
    try:

        text = str(text)
        text = myfont.render(text, True, color)
        screen.blit(text, (x, y))

    except:
        print('Font Error, saw it coming')


def main():
    running = True
    pg.init()

    pg.display.set_caption(CAPTION)
    pg.display.set_mode(SCREEN_SIZE)
    rect1 = rectangle()

    basicfont = pygame.font.SysFont(None, 48)
    text = basicfont.render('Choose your Forms')
    textrect = text.get_rect()



    running = True
    screen = pg.display.get_surface()
    pg.init()
    screen.fill((255, 255, 255))


    pg.display.update()
    clock.tick(40)



if __name__ == "__main__":
    main()