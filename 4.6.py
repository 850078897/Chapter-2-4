import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
frank = turtle.Turtle()
frank.color("blue")
frank.pensize(3)

def drawsb(sb, fv):
    for i in range(80):
        sb = sb+5
        frank.left(90)
        frank.forward(sb)
    
    
drawsb(5,10)