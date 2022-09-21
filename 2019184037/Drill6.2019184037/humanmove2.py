import math
from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move():
    math.sin(270 / 360 * 2 * math.pi)
    
x = 0
y = 0
while ( x < 800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(400,90)
    delay(0.01)

if x < '800':
    clear_canvas_now()
    grass.draw_now(move,y)
    delay(0.01)

    
        
close_canvas()
