import unittest
import tetris
import pygame as pg
import time
import copy

CAPTION = "Tetris"
SCREEN_SIZE = (1200, 1000)
YELLOW = pg.Color("yellow")
RED = pg.Color("red")
BLUE = pg.Color("blue")
BLACK = pg.Color("black")
WHITE = pg.Color("white")
GREEN = pg.Color('green')


class TestTetris(unittest.TestCase):

    def setUp(self):
        pg.init()
        pg.display.set_caption(CAPTION)
        pg.display.set_mode(SCREEN_SIZE)
        self.screen = pg.display.get_surface()
        self.screen.fill((75, 75, 75))
        self.clock = pg.time.Clock()

    def tearDown(self):
        pass

    def test_draw_circle_with_shape(self):
        cube = [[[0, 0], [0, 1], [1, 0], [1, 1]],
                [[0, 0], [0, 1], [1, 0], [1, 1]],
                [[0, 0], [0, 1], [1, 0], [1, 1]],
                [[0, 0], [0, 1], [1, 0], [1, 1]]]
        circle = tetris.CircleWithShape(RED, 65, 200, 10, 10, cube)
        circle.draw(self.screen)
        self.assertIsNotNone(circle)
        pg.display.update()
        time.sleep(1)

    def test_draw_square(self):
        square = tetris.Square(100, 150, 65, RED)
        square.draw(self.screen)
        self.assertIsNotNone(square)
        pg.display.update()
        time.sleep(1)

    def test_cube_move(self):
        cube_shapes = [[[0, 0], [0, 1], [1, 0], [1, 1]],
                [[0, 0], [0, 1], [1, 0], [1, 1]],
                [[0, 0], [0, 1], [1, 0], [1, 1]],
                [[0, 0], [0, 1], [1, 0], [1, 1]]]
        cube = tetris.Shape(0, 0, 15, copy.deepcopy(cube_shapes), BLACK, BLUE)
        self.assertIsNotNone(cube)
        cube.move_side(True, None)
        for indx_state, cube_state in enumerate(cube_shapes):
            for indx_coords, coords in cube_state:
                self.assertEqual(cube_shapes[indx_state][indx_coords][0] + 1, cube.states[indx_state][indx_coords][0])
        cube.move_side(False, None)
        cube.move_side(False, None)
        # cube.move_side(False, None)
        for indx_state, cube_state in enumerate(cube_shapes):
            for indx_coords, coords in cube_state:
                self.assertEqual(cube_shapes[indx_state][indx_coords][0] - 1, cube.states[indx_state][indx_coords][0])


        # for coords, i in cube_shape[0]:
        #     self.assertEqual(cube_shape[0][i][0]+1, coords[0])


    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

