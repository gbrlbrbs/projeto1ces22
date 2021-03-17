import pygame as pg

from data.components.Food import Food
from data.components.Snake import Snake
from data.components.draw_grid import draw_grid
from data.states.GameState import GameState

import data.constants as c


class Gameplay(GameState):
    def __init__(self):
        super().__init__()

    def startup(self, persistent):
        super().startup(persistent)
        restart = self.persist["restart"]
        if restart:
            self.restart()
        self.level = self.persist["level"]
        self.screen_color = pg.Color(c.colors[self.level - 1])
        text = "Gameplay. Level {}. Press ESC/P-pause, L-lose or W-win".format(self.level)
        self.title = self.font.render(text, True, pg.Color("gray10"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        if c.DEBUG:
            print(self.__class__.__name__, self.persist)

    def restart(self):
        self.snake = Snake()
        self.food = Food()

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
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                self.snake.turn(c.up)
            elif event.key == pg.K_DOWN:
                self.snake.turn(c.down)
            elif event.key == pg.K_LEFT:
                self.snake.turn(c.left)
            elif event.key == pg.K_RIGHT:
                self.snake.turn(c.right)

    def update(self, dt):
        collided = self.snake.move()
        if collided:
            last_game = {'level': self.level, 'score': self.snake.score}
            self.persist["last_game"] = last_game

            if self.snake.score >= 0:
                if self.level != len(c.maps):
                    new_level = self.level + 1
                    if new_level not in self.persist["unlocked_levels"]:
                        self.persist["unlocked_levels"].append(new_level)
                self.next_state = "WIN"
            else:
                self.next_state = "PLAY AGAIN"
            self.done = True
            return

        if self.snake.get_head_position() == self.food.position:
            self.snake.length += 1
            self.snake.score += 1
            self.food.randomize_position()

        score_text = "Score: {}".format(self.snake.score)
        self.score = self.font.render(score_text, True, pg.Color("gray10"))
        self.score_rect = self.score.get_rect(left=self.screen_rect.left)
        self.score_rect.move_ip(10, 10)

    def draw(self, surface):
        draw_grid(surface, c1=self.screen_color, c2=self.screen_color)
        self.snake.draw(surface, c1=self.screen_color)
        self.food.draw(surface, c1=self.screen_color)
        surface.blit(self.title, self.title_rect)
        surface.blit(self.score, self.score_rect)
