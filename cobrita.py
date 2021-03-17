# This code is licensed as CC0 1.0 (https://creativecommons.org/publicdomain/zero/1.0/legalcode).

import sys
import pygame as pg

from data.states.Credits import Credits
from data.states.Game import Game
from data.states.Gameplay import Gameplay
from data.states.Help import Help
from data.states.MapSelection import MapSelection
from data.states.Menu import Menu
from data.states.Paused import Paused
from data.states.PlayAgain import PlayAgain
from data.states.Win import Win


def main():
    pg.init()
    # size = 1280, 720
    size = 640, 360
    screen = pg.display.set_mode(size)
    states = {
        "MENU": Menu(),
        "MAP SELECTION": MapSelection(),
        "GAMEPLAY": Gameplay(),
        "PLAY AGAIN": PlayAgain(),
        "WIN": Win(),
        "PAUSED": Paused(),
        "HELP": Help(),
        "CREDITS": Credits()
    }
    game = Game(screen, states, "MENU")
    game.run()
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
