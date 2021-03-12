import random

import pygame
from pygame.math import Vector2


class Snake:
    def __init__(self):
        self.WIDTH = 10
        self.HEIGHT = 5

        self.LEFT = Vector2(-1, 0)
        self.DOWN = Vector2(0, 1)
        self.RIGHT = Vector2(1, 0)
        self.UP = Vector2(0, -1)

        self.DIRECTIONS = [self.LEFT, self.DOWN, self.RIGHT, self.UP]
        self.direction_index = 0
        self.length = 1

        self.head = Vector2(0, 0)
        self.positions = [self.head]

        self.score = 0

    def turn_left(self):
        self.direction_index = (self.direction_index - 1) % len(self.DIRECTIONS)

    def turn_right(self):
        self.direction_index = (self.direction_index + 1) % len(self.DIRECTIONS)

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * gridsize)) % screen_width), (cur[1] + (y * gridsize)) % screen_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((screen_width / 2), (screen_height / 2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize, gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)
