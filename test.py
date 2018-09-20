import os
import sys
import time

import pygame as pg

CAPTION = "4-Direction Movement with Animation"
SCREEN_SIZE = (600, 400)

BACKGROUND_COLOR = pg.Color("slategray")
BAR_COLOR = pg.Color("red")
COLOR_KEY = pg.Color("magenta")

DIRECT_DICT = {pg.K_LEFT: (-1, 0),
               pg.K_RIGHT: (1, 0),
               pg.K_UP: (0, -1),
               pg.K_DOWN: (0, 1)}


class Circle(object):

    def __init__(self, canvas, circleColor, x, y, rad, thickness):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.rad = rad
        self.circleColor = circleColor
        self.thickness = thickness

    def drawcircle(self):
       # cercle = canvas.create_oval(x - rad, y - rad, x + rad, y + rad, width=0, fill=cercleColor)
        pg.draw.circle(self.canvas, self.circleColor, (self.x, self.y), self.rad, self.thickness)





class Bar(object):

    def __init__(self, x, y, width, height, key_up, key_down):
        self.x = x
        self.y = y
        self.width = width
        self.height= height
        self.key_up = key_up
        self.key_down = key_down
        self.animate_fps = 144


    def get_event(self, event):
        """
        Handle events pertaining to player control.
        """
        if event.type == self.keyUp:
            self.add_direction(event.key)
        elif event.type == self.keyDown:
            self.pop_direction(event.key)

    def update(self, now, screen_rect):
        """
        Updates our player appropriately every frame.
        """
        self.adjust_images(now)
        if self.direction_stack:
            direction_vector = DIRECT_DICT[self.direction]
            self.rect.x += self.speed * direction_vector[0]
            self.rect.y += self.speed * direction_vector[1]
            self.rect.clamp_ip(screen_rect)

    def draw(self, surface):
        """
        Draws the player to the target surface.
        """

        self.rect = pg.draw.rect(surface, BAR_COLOR, [self.x, self.y, self.width, self.height], 5)


    def move(self, y_change, surface):
        self.rect.y +=y_change
        surface.blit(surface, self.rect)
        pg.time.Clock().tick(40)
        pg.display.update()

def event_action(evt):
    if evt.type == pg.KEYUP:
        if evt.key == pg.K_SPACE:
            print('up')
    if evt.type == pg.KEYDOWN:
        if evt.key == pg.K_SPACE:
            print('down')


def main():
    """
    Prepare our environment, create a display, and start the program.
    """
    running = True
    pg.init()



    global SKEL_IMAGE
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    pg.display.set_caption(CAPTION)
    pg.display.set_mode(SCREEN_SIZE)
    bar = Bar(10, 10, 20, 50,  pg.KEYUP, pg.KEYDOWN)
    bar1 = Bar(590, 80, 20, 50, pg.K_a, pg.K_q)
    screen = pg.display.get_surface()
    circle = Circle(screen, (0,0,255), 150, 50, 15,  3)
    circle.drawcircle()
    bar.draw(screen)
    bar1.draw(screen)
    pg.display.update()


    y_change = 0

    while running:



        for evt in pg.event.get():
            event_action(evt)
            if evt.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if evt.type == pg.KEYDOWN:
                if evt.key == pg.K_ESCAPE:
                    running = False
                elif evt.key == pg.K_DOWN:
                    print('key hit', Bar)
                    bar.move(50, screen)
                elif evt.key == pg.K_UP:
                    print('key hit', Bar)
                    y_change = -5



    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()