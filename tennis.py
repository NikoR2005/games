import os
import sys
import time

import pygame as pg


CAPTION = "4-Direction Movement with Animation"
SCREEN_SIZE = (600, 400)
SCREEN_SIZE_1 = (300, 200)

BACKGROUND_COLOR = pg.Color("slategray")
BAR_COLOR = pg.Color("red")
COLOR_KEY = pg.Color("magenta")



clock = pg.time.Clock()
pg.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pg.font.SysFont('Comic Sans MS', 30)
reset_key = pg.K_r

class Circle(object):

    v_x = 5
    v_y = 10

    def __init__(self, canvas, circleColor, x, y, rad, thickness, bar1, bar2):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.rad = rad
        self.circleColor = circleColor
        self.thickness = thickness
        self.bar1 = bar1
        self.bar2 = bar2


    def drawcircle(self, screen):
       # cercle = canvas.create_oval(x - rad, y - rad, x + rad, y + rad, width=0, fill=cercleColor)
        pg.draw.circle(screen, self.circleColor, (self.x, self.y), self.rad, self.thickness)
        print(self.x, self.y, self.y + self.rad, SCREEN_SIZE[1])
        if self.y + self.rad >= SCREEN_SIZE[1] or self.y <= self.rad:
            self.v_y = -self.v_y
        if self.x + self.rad >= SCREEN_SIZE[0] or self.x <= self.rad:
            self.v_x = -self.v_x

        if(self.x - self.rad <=  self.bar1.x + self.bar1.width and self.y >=  self.bar1.y and self.y <=  self.bar1.y +  self.bar1.height):
            self.v_x = -self.v_x
        if(self.x + self.rad >=  self.bar2.x and self.y >=  self.bar2.y and self.y <=  self.bar2.y +  self.bar2.height):
            self.v_x = -self.v_x
        if(SCREEN_SIZE[0] - self.x <= self.rad or self.x <= self.rad):
            self.v_x = 0
            self.v_y = 0


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
                self.rect.move_ip(0, -5)
                self.y -= 5
        if key[self.key_down]:
            print(self.y)
            if self.y < SCREEN_SIZE[1] - self.height:
                self.rect.move_ip(0, 5)
                self.y += 5



    def draw(self, screen):
        """
        Draws the player to the target surface.
        """
        pg.draw.rect(screen, (0, 0, 128), self.rect)


def text_to_screen(screen, text, x, y, size = 50,
            color = COLOR_KEY):
    try:

        text = str(text)
        text = myfont.render(text, True, color)
        screen.blit(text, (x, y))

    except:
        print('Font Error, saw it coming')

def main():
    """
    Prepare our environment, create a display, and start the program.
    """
    running = True
    pg.init()



    pg.display.set_caption(CAPTION)
    pg.display.set_mode(SCREEN_SIZE)

    bar1 = Bar(10, 10, 20, 150, pg.K_a, pg.K_q)
    bar2 = Bar(570, 80, 20, 150, pg.K_UP, pg.K_DOWN)
    screen = pg.display.get_surface()
    circle = Circle(screen, COLOR_KEY, 150, 50, 15,  3, bar1, bar2)

    pg.font.init()  # you have to call this at the start,
    # if you want to use this module.
    myfont = pg.font.SysFont('Comic Sans MS', 30)

#    screen.blit(bar.box_surface, (20, 10))

    pg.display.update()


    y_change = 0

    while running:

        for evt in pg.event.get():
            if evt.type == pg.KEYDOWN:
                if evt.key == pg.K_ESCAPE:
                    running = False
                if evt.key == pg.K_r:
                    print('r pressed')
                    circle.v_x = 5
                    circle.v_y = 10
                    circle.x = 300
                    circle.y = 200

        screen.fill((255, 255, 255))

        bar1.draw(screen)
        bar2.draw(screen)
        circle.drawcircle(screen)
        bar1.handle_keys()
        bar2.handle_keys()
        pg.display.update()
        pg.display.update()
        clock.tick(40)
        text_to_screen(screen, '1|2', 50, 50)


    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()