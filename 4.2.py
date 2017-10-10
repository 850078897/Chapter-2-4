import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
newbee = turtle.Turtle()
newbee.color("pink")
newbee.pensize(3)

def drawsquare(newbee, sz):
    for i in range(4):
        newbee.forward(size)
        newbee.left(90)
size = 20
a = 0
b = 0
for j in range(5):
    drawsquare(newbee, size)
    size = size + 20
    a = a - 10
    b = b - 10
    newbee.penup()
    newbee.goto(a, b)
    newbee.pendown()

        
wn.mainloop()
