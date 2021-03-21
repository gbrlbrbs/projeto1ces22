import sys

import pygame as pg

import data.constants as c

from data.states.Credits import Credits
from data.states.Gameplay import Gameplay
from data.states.Help import Help
from data.states.MapSelection import MapSelection
from data.states.Menu import Menu
from data.states.Paused import Paused
from data.states.PlayAgain import PlayAgain
from data.states.Win import Win
from data.states.statemachine.Game import Game

pg.init()
screen = pg.display.set_mode((c.screen_width, c.screen_height))
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


def main(initial_state, persist):
    game = Game(screen, states, initial_state, persist)
    game.run()
    pg.quit()
    sys.exit()
