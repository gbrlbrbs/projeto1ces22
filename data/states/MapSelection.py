import pygame as pg
from data.states.GameState import GameState
import data.constants as c


class MapSelection(GameState):
    def __init__(self):
        super().__init__()

    def startup(self, persistent):
        super().startup(persistent)
        for prop in ["level", "screen_color"]:
            if prop in self.persist:
                print("deletei {}".format(prop))
                del self.persist[prop]
        text = "Map Selection. Press a number 1-{} for gameplay or M-menu.".format(len(c.maps))
        self.title = self.font.render(text, True, pg.Color("gray10"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_m:
                self.next_state = "MENU"
                self.done = True
            elif pg.K_1 <= event.key <= pg.K_9:
                level = event.key - pg.K_1 + 1
                if 1 <= level <= len(c.maps):
                    self.next_state = "GAMEPLAY"
                    self.persist["level"] = level
                    self.persist["restart"] = True
                    self.persist["screen_color"] = c.colors[level - 1]
                    self.done = True

        elif event.type == pg.MOUSEBUTTONUP:
            pass

    def draw(self, surface):
        surface.fill(pg.Color("black"))
        surface.blit(self.title, self.title_rect)
