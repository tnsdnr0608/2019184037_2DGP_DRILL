from pico2d import *
import math


open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

rectangle = 0
turn = 0
x, y = 400, 90

while(1):
    clear_canvas_now()
    grass.draw_now(400,30)

    if turn % 2 == 0:
        if rectangle % 4 == 0:
            if x >= 800:
                rectangle += 1
            else:
                x += 2

        elif rectangle % 4 == 1:
            if y >= 600:
                rectangle += 1
            else:
                y += 2

        elif rectangle % 4 == 2:
            if x <= 0:
                rectangle += 1
            else:
                x -= 2

        else:
            if y <= 90:
                if x < 400:
                    x += 2
                else:
                    rectangle += 1
                    turn += 1

            else:
                y -= 2


    character.draw_now(x, y)
    delay(0.01)

close_canvas()
