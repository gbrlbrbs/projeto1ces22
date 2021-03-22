import sys

import pygame as pg

import data.constants as c
import data.state_literals as sl
import data.persist_literals as pl

from data.states.Credits import Credits
from data.states.Gameplay import Gameplay
from data.states.Help import Help
from data.states.MapSelection import MapSelection
from data.states.Menu import Menu
from data.states.Paused import Paused
from data.states.PlayAgain import PlayAgain
from data.states.Win import Win
from data.states.statemachine.Game import Game
from data.states.statemachine.Transitions import Transitions

pg.init()
_screen = pg.display.set_mode((c.screen_width, c.screen_height))
states = {
    sl.MENU: Menu(),
    sl.MAP_SELECTION: MapSelection({1}),
    sl.GAMEPLAY: Gameplay(),
    sl.PLAY_AGAIN: PlayAgain(),
    sl.WIN: Win(),
    sl.PAUSED: Paused(),
    sl.HELP: Help(),
    sl.CREDITS: Credits()
}

_states_keys = list(states.keys())
_transitions_origins = _states_keys.copy()
for x in [sl.GAMEPLAY, sl.WIN]:
    _transitions_origins.remove(x)

transitions = Transitions(_states_keys, _transitions_origins)


def _set_transitions():
    transitions.set(origin=sl.MENU, dest=sl.MAP_SELECTION, key=pg.K_m)
    transitions.set(origin=sl.MENU, dest=sl.CREDITS, key=pg.K_c)
    transitions.set(origin=sl.MENU, dest=sl.HELP, key=pg.K_h)

    transitions.set(origin=sl.CREDITS, dest=sl.MENU, key=pg.K_m)

    transitions.set(origin=sl.HELP, dest=sl.MENU, key=pg.K_m)

    transitions.set(origin=sl.PAUSED, dest=sl.GAMEPLAY, key=pg.K_c)
    transitions.set(origin=sl.PAUSED, dest=sl.MAP_SELECTION, key=pg.K_m)

    transitions.set(origin=sl.PLAY_AGAIN, dest=sl.GAMEPLAY, key=pg.K_y)
    transitions.set(origin=sl.PLAY_AGAIN, dest=sl.MAP_SELECTION, key=pg.K_n)

    transitions.set(origin=sl.MAP_SELECTION, dest=sl.MENU, key=pg.K_m)
    for lvl in range(1, 10):
        key = pg.K_1 - 1 + lvl
        transitions.set(origin=sl.MAP_SELECTION, dest=sl.GAMEPLAY, key=key,
                        level=lvl, restart=True)


def main(initial_state, persist=None):
    if persist is None:
        persist = {}
    _set_transitions()
    game = Game(_screen, states, initial_state, persist)
    game.run()
    pg.quit()
    sys.exit()
