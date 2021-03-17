import pygame as pg
from data.states.GameState import GameState
import data.constants as c


class PlayAgain(GameState):
    def __init__(self):
        super().__init__()

    def startup(self, persistent):
        super().startup(persistent)
        text = "You Lost. Play Again? Press Y-yes or N-no."
        self.title = self.font.render(text, True, pg.Color("gray10"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        if c.DEBUG:
            print(self.__class__.__name__, self.persist)

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_y:
                self.next_state = "GAMEPLAY"
                self.done = True
            elif event.key == pg.K_n:
                self.next_state = "MAP SELECTION"
                self.done = True
        elif event.type == pg.MOUSEBUTTONUP:
            pass

    def draw(self, surface):
        surface.fill(pg.Color("black"))
        surface.blit(self.title, self.title_rect)
