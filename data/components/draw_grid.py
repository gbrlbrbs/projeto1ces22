import pygame
import data.constants as c


def draw_grid(surface, c1=(93, 216, 228), c2=(84, 194, 205)):
    for y in range(0, int(c.grid_height)):
        for x in range(0, int(c.grid_width)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * c.gridsize, y * c.gridsize), (c.gridsize, c.gridsize))
                pygame.draw.rect(surface, c1, r)
            else:
                rr = pygame.Rect((x * c.gridsize, y * c.gridsize), (c.gridsize, c.gridsize))
                pygame.draw.rect(surface, c2, rr)
