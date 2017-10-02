import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Hello, Alex!")
tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)
for xs in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    tess.left(xs)
    tess.forward(100)
print (tess.heading())