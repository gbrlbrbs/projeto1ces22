import pygame
import pygame_menu
import copied

levels = ['Cubol', 'Melas', 'Deuses vs. bixos', 'Cachorrão', 'Olimpo']

pygame.init()
surface = pygame.display.set_mode((800, 600))


def set_level(value, difficulty):
    print(value, difficulty)
    pass


def start_the_game():
    copied.game_loop()
    pass


menu = pygame_menu.Menu(600, 800, 'CobrITA',
                        theme=pygame_menu.themes.THEME_BLUE)

menu.add_selector('Mapa :', [(l, i) for (i, l) in enumerate(levels)], onchange=set_level)
menu.add_button('Play', start_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)

pygame.quit()
quit()
