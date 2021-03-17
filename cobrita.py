# This code is licensed as CC0 1.0 (https://creativecommons.org/publicdomain/zero/1.0/legalcode).

import sys
import pygame as pg

from src.engine.Game import Game
from src.engine.Gameplay import Gameplay
from src.engine.SplashScreen import SplashScreen


def main():
    pg.init()
    screen = pg.display.set_mode((1280, 720))
    states = {"SPLASH": SplashScreen(),
              "GAMEPLAY": Gameplay()}
    game = Game(screen, states, "SPLASH")
    game.run()
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
