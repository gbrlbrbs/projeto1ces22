import pygame as pg

import data
from data.states.statemachine.GameState import GameState
import data.persist_literals as pl
import data.state_literals as sl


class Menu(GameState):
    def __init__(self):
        super().__init__()

    def startup(self, persistent):
        super().startup(persistent)
        menus = ["Main Menu", "Map Selection", "Help", "Credits"]
        f = pg.font.Font(None, 30)
        self.title = f.render(menus[0], True, pg.Color("blue"))
        self.mapselec = self.font.render(menus[1], True, pg.Color("red"))
        self.help = self.font.render(menus[2], True, pg.Color("yellow"))
        self.credits = self.font.render(menus[3], True, pg.Color(245, 245, 245))
        self.title_center = (self.screen_rect.center[0] - 10, self.screen_rect.center[1] - 30)
        self.credits_center = (self.screen_rect.center[0] - 10, self.screen_rect.center[1] + 20)
        self.help_center = (self.screen_rect.center[0] - 10, self.screen_rect.center[1] + 40)
        self.mapselec_center = (self.screen_rect.center[0] - 50, self.screen_rect.center[1])
        self.title_rect = self.title.get_rect(center=self.title_center)
        self.help_rect = self.help.get_rect(center=self.help_center)
        self.credits_rect = self.credits.get_rect(center=self.credits_center)
        self.mapselec_rect = self.help.get_rect(center=self.mapselec_center)

    def draw(self, surface):
        surface.fill(pg.Color(33, 33, 33))
        surface.blit(self.title, self.title_rect)
        surface.blit(self.mapselec, self.mapselec_rect)
        surface.blit(self.help, self.help_rect)
        surface.blit(self.credits, self.credits_rect)


def main(start_map):
    ms = data.states[sl.MAP_SELECTION]
    ms.unlock_map(start_map)
    persist = {pl.restart: True, pl.selected_map: start_map}
    data.main("MENU", persist=persist)


if __name__ == "__main__":
    main(start_map='lvl1')
