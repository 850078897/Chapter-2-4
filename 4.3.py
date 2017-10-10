import turtle

def draw_poly(turt, sidenum, sz):
    for i in range(sidenum):
        turt.forward(sz)
        turt.left(360/sidenum)

turt = turtle.Turtle()
draw_poly(turt, 8, 50)