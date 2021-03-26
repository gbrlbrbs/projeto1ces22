maps = {'1', '2', '3', '4', '5'}
colors = ['red', 'blue', 'green', 'pink', 'cyan']

screen_width = 480
screen_height = 480

fps = 10

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

gridsize = 16
grid_width = screen_width / gridsize
grid_height = screen_height / gridsize

if not __debug__:
    min_score = 6
else:
    min_score = 0
