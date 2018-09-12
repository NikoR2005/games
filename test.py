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

    def __init__(self, canvas, x, y, rad, cercleColor):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.rad = rad
        self.cercleColor = cercleColor

    def drawcircle(canvas, x, y, rad, cercleColor):
        cercle = canvas.create_oval(x - rad, y - rad, x + rad, y + rad, width=0, fill=cercleColor)





class Bar(object):

    def __init__(self, width, height, from_left, key_up, key_down):
        self.width = width
        self.height= height
        self.from_left = from_left  # the distance from the left side of the screen.
        self.key_up = key_up
        self.key_down = key_down
        self.animate_fps = 7


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

        pg.draw.rect(surface, BAR_COLOR, [10, self.from_left, self.width, self.height], 5)
        pg.draw.rect(surface, BAR_COLOR, [570, self.from_left, self.width, self.height], 5)




def main():
    """
    Prepare our environment, create a display, and start the program.
    """
    global SKEL_IMAGE
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    pg.display.set_caption(CAPTION)
    pg.display.set_mode(SCREEN_SIZE)
    bar = Bar(20, 50, 10, pg.KEYUP, pg.KEYDOWN)
    bar1 = Bar(20, 50, 570, pg.K_a, pg.K_q)
    screen = pg.display.get_surface()
    bar.draw(screen)
    pg.display.update()
    bar1.draw(screen)
    pg.display.update()
    time.sleep(10)


    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()