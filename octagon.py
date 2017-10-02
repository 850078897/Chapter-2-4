#octagon
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Hello, Alex!")
tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)
for i in range(8):
    tess.forward(100)
    tess.left(45)
tess.hideturtle()