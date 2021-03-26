import pygame as pg

import data
from data.states.statemachine.GameState import GameState
import data.persist_literals as pl
import data.state_literals as sl


class Menu(GameState):
    def __init__(self):
        super().__init__()

    def startup(self, persistent):
        self.text = "Menu. Press M-map, H-help or C-credits."
        super().startup(persistent)

    def draw(self, surface):
        surface.fill(pg.Color("black"))
        surface.blit(self.title, self.title_rect)


def main(start_map):
    ms = data.states[sl.MAP_SELECTION]
    ms.unlock_map(start_map)
    persist = {pl.restart: True, pl.selected_map: start_map}
    data.main("MENU", persist=persist)


if __name__ == "__main__":
    main(start_map='lvl1')
