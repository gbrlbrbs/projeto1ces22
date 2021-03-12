import pygame
from pygame.math import Vector2


class Snake:
    def __init__(self):
        self.WIDTH = 7
        self.HEIGHT = 5
        self.head = Vector2(0, 0)
        self.body = [self.head]
        self.size = 1

        self.DIRECTIONS = [Vector2(1, 0), Vector2(0, -1), Vector2(-1, 0), Vector2(0, 1)]
        self.direction_index = 0
        self.speed = 1

    def direction(self):
        return self.DIRECTIONS[self.direction_index]

    def velocity(self):
        return self.speed * self.direction()

    def move(self):
        velocity = self.velocity()
        self.head.x += velocity.x
        self.head.y += velocity.y
        self.body.append(self.head)
        if self.size < len(self.body):
            self.body.pop()

    def turn_left(self):
        self.direction_index = (self.direction_index - 1) % 4

    def turn_right(self):
        self.direction_index = (self.direction_index + 1) % 4

    def print(self):
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                if Vector2(i, j) in self.body:
                    print("1", end='')
                else:
                    print("0", end='')
            print()

    def __str__(self):
        return str(self.head)


s = Snake()
commands = "MMRMMLMM"

for c in commands:
    if c == "M":
        s.move()
    elif c == "R":
        s.turn_right()
    elif c == "L":
        s.turn_left()
    s.print()
    print()
