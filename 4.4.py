import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
wn.bgcolor("lightgreen")
tess.color("blue")
tess.pensize(3)
def make_pattom(turt, sz):
    for i in range(16):
        tess.left(360/16)
        for i in range(4):
            tess.forward(sz)
            tess.left(90)
        
make_pattom(tess, 100)