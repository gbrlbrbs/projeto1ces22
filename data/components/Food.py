import random

import pygame
import data.constants as c


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, c.grid_width - 1) *
                         c.gridsize, random.randint(0, c.grid_height - 1) * c.gridsize)

    def draw(self, surface, c1=(93, 216, 228)):
        r = pygame.Rect((self.position[0], self.position[1]), (c.gridsize, c.gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, c1, r, 1)
