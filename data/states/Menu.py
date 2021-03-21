import pygame as pg

import data
from data.states.statemachine.GameState import GameState
import data.constants as c


class Menu(GameState):
    def __init__(self):
        super().__init__()

    def startup(self, persistent):
        super().startup(persistent)
        text = "Menu. Press M-map, H-help or C-credits."
        self.title = self.font.render(text, True, pg.Color("gray50"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        if c.DEBUG:
            print(self.__class__.__name__, self.persist)

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_m:
                self.next_state = "MAP SELECTION"
                self.done = True
            elif event.key == pg.K_c:
                self.next_state = "CREDITS"
                self.done = True
            elif event.key == pg.K_h:
                self.next_state = "HELP"
                self.done = True

        elif event.type == pg.MOUSEBUTTONUP:
            pass

    def draw(self, surface):
        surface.fill(pg.Color("black"))
        surface.blit(self.title, self.title_rect)


def main():
    data.main("MENU", persist={'unlocked_levels': [1]})


if __name__ == "__main__":
    main()
