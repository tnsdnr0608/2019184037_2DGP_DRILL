import turtle

turtle.shape('turtle')

def up():
    turtle.setheading(90)
    turtle.stamp()
    turtle.forward(50)
    turtle.pendown()
    
def left():
    turtle.setheading(180)
    turtle.stamp()
    turtle.forward(50)
    turtle.pendown()

def down():
    turtle.setheading(-90)
    turtle.stamp()
    turtle.forward(50)
    turtle.pendown()

def light():
    turtle.setheading(360)
    turtle.stamp()
    turtle.forward(50)
    turtle.pendown()

def restart():
    turtle.reset()

    
turtle.onkey(up, 'w')
turtle.onkey(left, 'a')
turtle.onkey(down, 's')
turtle.onkey(light, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()


