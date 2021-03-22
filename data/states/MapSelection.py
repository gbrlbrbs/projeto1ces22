import pygame as pg

import data.persist_literals as pl
from data.states.statemachine.GameState import GameState


class MapSelection(GameState):
    def __init__(self, unlocked_levels=None):
        super().__init__()
        if unlocked_levels is None:
            unlocked_levels = {1}
        self.unlocked_levels = unlocked_levels

    def startup(self, persistent):
        if pl.new_unlocked_levels in persistent:
            self.unlock_levels(persistent[pl.new_unlocked_levels])
        self.text = "Map Selection. Press {} for gameplay or M-menu.".format(self.unlocked_levels)
        super().startup(persistent)

    def draw(self, surface):
        surface.fill(pg.Color("black"))
        surface.blit(self.title, self.title_rect)

    def unlock_levels(self, new_levels):
        self.unlocked_levels = self.unlocked_levels | new_levels
