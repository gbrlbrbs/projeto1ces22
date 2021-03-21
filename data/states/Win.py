import pygame as pg
from data.states.statemachine.GameState import GameState
import data.constants as c


class Win(GameState):
    def __init__(self):
        super().__init__()
        self.next_state = "MAP SELECTION"

    def startup(self, persistent):
        super().startup(persistent)
        text = "You won! Congratulations!! Press any key to continue."
        self.title = self.font.render(text, True, pg.Color("gray50"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        if c.DEBUG:
            print(self.__class__.__name__, self.persist)

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type in [pg.KEYUP, pg.MOUSEBUTTONUP]:
            self.done = True

    def draw(self, surface):
        surface.fill(pg.Color("black"))
        surface.blit(self.title, self.title_rect)
