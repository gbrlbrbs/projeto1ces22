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


class TimerThread(object):

    def __init__(self, interval, function, args=None, kwargs=None):
        """
        Runs the function at a specified interval with given arguments.
        """
        self.interval = interval
        if args is None:
            args = []
        if kwargs is None:
            kwargs = {}
        self.function = partial(function, *args, **kwargs)
        self.running = False
        self._timer = None

    def __call__(self):
        """
        Handler function for calling the partial and continuing.
        """
        self.running = False  # mark not running
        self.start()  # reset the timer for the next go
        self.function()  # call the partial function

    def start(self):
        """
        Starts the interval and lets it run.
        """
        if self.running:
            # Don't start if we're running!
            return

            # Create the timer object, start and set state.
        self._timer = Timer(self.interval, self)
        self._timer.start()
        self.running = True

    def stop(self):
        """
        Cancel the interval (no more function calls).
        """
        if self._timer:
            self._timer.cancel()
        self.running = False
        self._timer = None


class PowerUpFactory:
    """
    Class to control the power-up creation
    """
    def __init__(self, interval, items, snake_positions):
        """
        Initializes the PowerUpFactory object

        :param interval: time (in seconds) to call create method]
        :param items: dict that contains the possible power-ups with different powers and probabilities
        :param snake_positions: follows snake's positions
        """
        self.interval = interval
        self.dict = items
        self.timer = TimerThread(self.interval, self.create, args=snake_positions)
        # list of active powerups
        self.powerup = []

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def create(self, snake_positions):
        """
        Simplified creation method
        """
        k = random()
        if c.DEBUG:
            print("factory running")
        if k > 0.5:
            print("entered")
            self.powerup.append(PowerUp())
            end = len(self.powerup) - 1
            self.powerup[end].randomize_position(snake_positions)
            # need to change this
            self.powerup[end].draw(pg.display.set_mode((c.screen_width, c.screen_height)))
