from random import randint, random
from threading import Timer
from functools import partial
import pygame as pg
import data.constants as c


class PowerUp:
    def __init__(self):
        self.position = (0, 0)
        self.color = (66, 135, 245)
        self.randomize_position()

    def randomize_position(self, snake=None):
        if snake is None:
            snake = []
        while True:
            self.position = (randint(0, c.grid_width - 1) *
                             c.gridsize, randint(0, c.grid_height - 1) * c.gridsize)
            # item position can't override snake's body
            if self.position not in snake:
                return


def draw(self, surface, c1=(93, 216, 228)):
    r = pg.Rect((self.position[0], self.position[1]), (c.gridsize, c.gridsize))
    pg.draw.rect(surface, self.color, r)
    pg.draw.rect(surface, c1, r, 1)
