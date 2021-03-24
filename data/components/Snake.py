import random
import sys

import pygame

import data.constants as c


class Snake:
    def __init__(self):
        self.length = 1
        self.head_direction = random.choice([c.up, c.down, c.left, c.right])
        self.positions = [(c.screen_width/2, c.screen_height/2)]
        self.directions = [self.head_direction]
        self.color = (17, 24, 4)
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.head_direction:
            return
        else:
            self.head_direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.head_direction
        new = (cur[0] + (x * c.gridsize), cur[1] + (y * c.gridsize))
        xn, yn = new
        # checks if the snake collided with map borders
        if xn < 0 or xn >= c.screen_width or yn >= c.screen_height or yn < 0:
            return True
        # checks if the snake collided with itself
        if len(self.positions) > 2 and new in self.positions[2:]:
            return True
        else:
            self.positions.insert(0, new)
            self.directions.insert(0, (x, y))
            if len(self.positions) > self.length:
                self.positions.pop()
            if len(self.directions) > self.length:
                self.directions.pop()
            return False

    def reset(self):
        self.length = 1
        self.head_direction = random.choice([c.up, c.down, c.left, c.right])
        self.positions = [(c.screen_width/2, c.screen_height/2)]
        self.directions = [self.head_direction]
        self.score = 0

    def draw(self, surface, c1=(93, 216, 228)):
        for p, d in zip(self.positions, self.directions):
            # code for using up, down, left, right sprites
            r = pygame.Rect((p[0], p[1]), (c.gridsize, c.gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, c1, r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(c.up)
                elif event.key == pygame.K_DOWN:
                    self.turn(c.down)
                elif event.key == pygame.K_LEFT:
                    self.turn(c.left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(c.right)
