import pygame as pg
from data.states.statemachine.GameState import GameState
import data.constants as c


class MapSelection(GameState):
    def __init__(self):
        super().__init__()

    def startup(self, persistent):
        self.text = "Map Selection. Press {} for gameplay or M-menu.".format(self.unlocked)
        super().startup(persistent)
        # sets unlocked levels
        self.unlocked = self.persist["unlocked_levels"]

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYUP:
            # return to menu
            if event.key == pg.K_m:
                self.next_state = "MENU"
                self.done = True
            # method to choose the map
            elif pg.K_1 <= event.key <= pg.K_9:
                level = event.key - pg.K_1 + 1
                if 1 <= level <= len(c.maps) and level in self.unlocked:
                    self.next_state = "GAMEPLAY"
                    self.persist["level"] = level
                    self.persist["restart"] = True
                    self.done = True

        elif event.type == pg.MOUSEBUTTONUP:
            pass

    def draw(self, surface):
        surface.fill(pg.Color("black"))
        surface.blit(self.title, self.title_rect)
