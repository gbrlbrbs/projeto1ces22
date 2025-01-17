import pygame as pg

from data.states.statemachine.GameState import GameState


class Paused(GameState):
    def __init__(self):
        super().__init__()

    def startup(self, persistent):
        self.text = "Paused. Press C-continue or M-map."
        super().startup(persistent)

    def cleanup(self):
        if self.next_state != "GAMEPLAY":
            self.persist.pop("level")
            self.persist.pop("restart")

    def cleanup(self):
        if self.next_state != "GAMEPLAY":
            self.persist.pop("level")
            self.persist.pop("restart")

    def draw(self, surface):
        surface.fill(pg.Color("black"))
        surface.blit(self.title, self.title_rect)
