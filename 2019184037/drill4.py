import turtle

turtle.penup()
turtle.goto(0,-200)
turtle.pendown()

count = 4
while (count > 0):
    turtle.forward(500)
    turtle.left(90)
    count = count - 1

turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.forward(500)


turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.forward(500)

turtle.penup()
turtle.goto(0,100)
turtle.pendown()
turtle.forward(500)

turtle.penup()
turtle.goto(0,200)
turtle.pendown()
turtle.forward(500)


turtle.penup()
turtle.goto(100,-200)
turtle.left(90)
turtle.pendown()
turtle.forward(500)

turtle.penup()
turtle.goto(200,-200)
turtle.pendown()
turtle.forward(500)

turtle.penup()
turtle.goto(300,-200)
turtle.pendown()
turtle.forward(500)

turtle.penup()
turtle.goto(400,-200)
turtle.pendown()
turtle.forward(500)

turtle.exitonclick()

