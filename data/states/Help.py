import pygame as pg

from data.states.statemachine.GameState import GameState


class Help(GameState):
    def __init__(self):
        super().__init__()

    def startup(self, persistent):
        self.text = "Help. Press M-menu."
        super().startup(persistent)

    def draw(self, surface):
        surface.fill(pg.Color("black"))
        surface.blit(self.title, self.title_rect)
