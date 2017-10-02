import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Hello, Alex!")
tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)
tess.hideturtle(40)
tess.showturtle(10)
for i in range(12):
    tess.left(30)
    tess.forward(50)

