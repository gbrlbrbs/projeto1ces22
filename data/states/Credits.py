import pygame as pg

from data.states.statemachine.GameState import GameState


class Credits(GameState):
    def __init__(self):
        super().__init__()

    def startup(self, persistent):
        self.text = "Credits. Press M-menu."
        super().startup(persistent)

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_m:
                self.next_state = "MENU"
                self.done = True
        elif event.type == pg.MOUSEBUTTONUP:
            pass

    def draw(self, surface):
        surface.fill(pg.Color("black"))
        surface.blit(self.title, self.title_rect)
