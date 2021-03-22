import pygame as pg

import data
from data.states.statemachine.GameState import GameState


class Menu(GameState):
    def __init__(self):
        super().__init__()

    def startup(self, persistent):
        self.text = "Menu. Press M-map, H-help or C-credits."
        super().startup(persistent)

    def draw(self, surface):
        surface.fill(pg.Color("black"))
        surface.blit(self.title, self.title_rect)


def main():
    data.main("MENU")


if __name__ == "__main__":
    main()
