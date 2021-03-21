import pygame as pg

import data
from data.components.Food import Food
from data.components.PowerUpFactory import PowerUpFactory
from data.components.Snake import Snake
from data.components.draw_grid import draw_grid
from data.states.statemachine.GameState import GameState

import data.constants as c


class Gameplay(GameState):
    def __init__(self):
        super().__init__()

    def startup(self, persistent):
        super().startup(persistent)
        self.level = self.persist["level"]
        self.text = "Gameplay. Level {}. Press ESC/P-pause".format(self.level)
        self.title = self.font.render(self.text, True, pg.Color("gray20"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.screen_color = pg.Color(c.colors[self.level - 1])

        restart = self.persist["restart"]
        if restart:
            self.restart()

        self.factory.start()

    def restart(self):
        self.snake = Snake()
        self.food = Food()
        self.factory = PowerUpFactory(5, {}, self.snake.positions)

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.factory.stop()
            self.quit = True
        elif event.type == pg.MOUSEBUTTONUP:
            self.title_rect.center = event.pos
        elif event.type == pg.KEYUP:
            if event.key == pg.K_c:
                self.collided()
            elif event.key in [pg.K_ESCAPE, pg.K_p]:
                self.next_state = "PAUSED"
                self.persist["restart"] = False
                self.factory.stop()
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
            self.collided()
            return

        if self.snake.get_head_position() == self.food.position:
            self.snake.length += 1
            self.snake.score += 1
            self.food.randomize_position(self.snake.positions)

        score_text = "Score: {}".format(self.snake.score)
        self.score = self.font.render(score_text, True, pg.Color("gray10"))
        self.score_rect = self.score.get_rect(left=self.screen_rect.left)
        self.score_rect.move_ip(10, 10)

    def collided(self):
        self.factory.stop()
        last_game = {'level': self.level, 'score': self.snake.score}
        self.persist["last_game"] = last_game

        if self.snake.score >= c.min_score:
            if self.level != len(c.maps):
                new_level = self.level + 1
                if new_level not in self.persist["unlocked_levels"]:
                    self.persist["unlocked_levels"].append(new_level)
            self.next_state = "WIN"
        else:
            self.next_state = "PLAY AGAIN"
        self.done = True

    def cleanup(self):
        self.factory.stop()
        if self.next_state not in ["PAUSED", "PLAY AGAIN"]:
            self.persist.pop("level")
            self.persist.pop("restart")

    def draw(self, surface):
        draw_grid(surface, c1=self.screen_color, c2=self.screen_color)
        self.snake.draw(surface, c1=self.screen_color)
        self.food.draw(surface, c1=self.screen_color)
        # draw powerups
        for p in self.factory.collectable_powerups:
            p.draw(surface, c1=self.screen_color)
        surface.blit(self.title, self.title_rect)
        surface.blit(self.score, self.score_rect)


def main(level):
    persist = {'restart': True, 'level': level,
               'unlocked_levels': [1, 2, 3, 4, 5]}
    data.main("GAMEPLAY", persist=persist)


if __name__ == "__main__":
    main(level=5)
