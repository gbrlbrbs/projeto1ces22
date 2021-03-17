import pygame as pg
from data.states.GameState import GameState


class Gameplay(GameState):
    def __init__(self):
        super().__init__()

    def startup(self, persistent):
        super().startup(persistent)
        restart = self.persist["restart"]
        if restart:
            self.restart()
        color = self.persist["screen_color"]
        self.screen_color = pg.Color(color)
        level = self.persist["level"]
        text = "Gameplay. Level {}. Press ESC/P-pause, L-lose or W-win".format(level)
        self.title = self.font.render(text, True, pg.Color("gray10"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)

    def restart(self):
        self.rect = pg.Rect((0, 0), (64, 64))
        self.x_velocity = 10

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.MOUSEBUTTONUP:
            self.title_rect.center = event.pos
        elif event.type == pg.KEYUP:
            if event.key == pg.K_l:
                self.next_state = "PLAY AGAIN"
                self.persist["restart"] = True
                self.done = True
            elif event.key == pg.K_w:
                self.next_state = "WIN"
                self.persist["restart"] = True
                self.done = True
            elif event.key in [pg.K_ESCAPE, pg.K_p]:
                self.next_state = "PAUSED"
                self.persist["restart"] = False
                self.done = True

    def update(self, dt):
        self.rect.move_ip(self.x_velocity, 0)
        if (self.rect.right > self.screen_rect.right
                or self.rect.left < self.screen_rect.left):
            self.x_velocity *= -1
            self.rect.clamp_ip(self.screen_rect)

    def draw(self, surface):
        surface.fill(self.screen_color)
        surface.blit(self.title, self.title_rect)
        pg.draw.rect(surface, pg.Color("darkgreen"), self.rect)
