import os
import sys
import time

import pygame as pg

CAPTION = "4-Direction Movement with Animation"
SCREEN_SIZE = (600, 400)

BACKGROUND_COLOR = pg.Color("slategray")
BAR_COLOR = pg.Color("red")
COLOR_KEY = pg.Color("magenta")



clock = pg.time.Clock()


class Circle(object):

    v_x = 5
    v_y = 10

    def __init__(self, canvas, circleColor, x, y, rad, thickness):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.rad = rad
        self.circleColor = circleColor
        self.thickness = thickness

    def drawcircle(self, screen):
       # cercle = canvas.create_oval(x - rad, y - rad, x + rad, y + rad, width=0, fill=cercleColor)
        pg.draw.circle(screen, self.circleColor, (self.x, self.y), self.rad, self.thickness)
        print(self.x, self.y, self.y + self.rad, SCREEN_SIZE[1])
        if self.y + self.rad >= SCREEN_SIZE[1] or self.y <= self.rad:
            self.v_y = -self.v_y
        if self.x + self.rad >= SCREEN_SIZE[0] or self.x <= self.rad:
            self.v_x = -self.v_x




        self.x += self.v_x
        self.y += self.v_y

class Bar(object):

    def __init__(self, x, y, width, height, key_up, key_down):
        self.x = x
        self.y = y
        self.width = width
        self.height= height
        self.key_up = key_up
        self.key_down = key_down
        self.animate_fps = 144
        self.bar_size = (24, 96)
        self.rect = pg.rect.Rect((self.x, self.y, self.width, self.height))

    def handle_keys(self):
        key = pg.key.get_pressed()

        if key[self.key_up]:
            print(self.y)
            if self.y > 0:
                self.rect.move_ip(0, -1)
                self.y -= 1
        if key[self.key_down]:
            print(self.y)
            if self.y < SCREEN_SIZE[1] - self.height:
                self.rect.move_ip(0, 1)
                self.y += 1



    def draw(self, screen):
        """
        Draws the player to the target surface.
        """
        pg.draw.rect(screen, (0, 0, 128), self.rect)




def main():
    """
    Prepare our environment, create a display, and start the program.
    """
    running = True
    pg.init()

    pg.display.set_caption(CAPTION)
    pg.display.set_mode(SCREEN_SIZE)
    bar = Bar(10, 10, 20, 50,  pg.K_UP, pg.K_DOWN)
    bar1 = Bar(570, 80, 20, 50, pg.K_a, pg.K_q)
    screen = pg.display.get_surface()
    circle = Circle(screen, COLOR_KEY, 150, 50, 15,  3)



#    screen.blit(bar.box_surface, (20, 10))

    pg.display.update()


    y_change = 0

    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                break
                running = False

        screen.fill((255, 255, 255))

        bar.draw(screen)
        bar1.draw(screen)
        circle.drawcircle(screen)
        bar.handle_keys()
        bar1.handle_keys()
        pg.display.update()
        pg.display.update()
        clock.tick(40)


    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()