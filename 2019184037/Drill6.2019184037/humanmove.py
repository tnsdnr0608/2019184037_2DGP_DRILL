import math
from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
while ( x < 800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x, 90)
    x += 2
    delay(0.01)
y = 0
while ( y < 800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(750,y)
    y += 2
    delay(0.01)

x = 0
while ( x < 800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x, 550)
    x += 2
    delay(0.01)

y = 0
while ( y < 800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(30,y)
    y += 2
    delay(0.01)

close_canvas()

