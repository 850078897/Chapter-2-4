import turtle
sz = 20
def drawsquare(newbee, sz):
    for i in range(5):
        newbee.penup()
        newbee.forward(50)
        newbee.pendown()
        for i in range(4):
            newbee.forward(sz)
            newbee.left(90)
            



wn = turtle.Screen()
wn.bgcolor("lightgreen")
newbee = turtle.Turtle()
newbee.color("pink")
newbee.pensize(3)

drawsquare(newbee, sz)