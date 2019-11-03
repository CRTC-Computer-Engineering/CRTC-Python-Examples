penup()
setposition(-200,-200)
speed(0)
def draw_square():
    for i in range(4):
        pendown()
        forward(50)
        left(90)
def draw_row():
    for i in range(8):
        draw_square()
        penup()
        forward(50)
def draw_sidewalk():
    for i in range(4):
        draw_row()
        left(90)
draw_sidewalk()