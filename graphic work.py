import turtle
a=0
b=0
turtle.bgcolor("black")
turtle.speed(1000)
turtle.pencolor("lightgreen")
turtle.penup()
turtle.goto(0,200)
turtle.pendown()


while True:
    turtle.forward(a)
    turtle.right(b)
    a+=3
    b+=1
    if b == 200:
        break
turtle.exitonclick()






