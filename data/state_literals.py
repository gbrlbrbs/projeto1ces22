import re

GAMEPLAY = "GAMEPLAY"
MENU = "MENU"
MAP_SELECTION = "MAP SELECTION"
CREDITS = "CREDITS"
PLAY_AGAIN = "PLAY AGAIN"
HELP = "HELP"
WIN = "WIN"
PAUSED = "PAUSED"

pattern = re.compile(r'(?<!^)(?=[A-Z])')


def pascal2upper(pascal):
    upper = pattern.sub(' ', pascal).upper()
    return upper


def upper2pascal(upper):
    pascal = upper.title().replace(' ', '')
    return pascal
