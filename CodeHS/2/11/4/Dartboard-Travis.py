speed(0)
radius = 25
circle(radius)
def init():
    penup()
    right(90)
    forward(25)
    left(90)
for i in range(3):
    init()
    pendown()
    radius = radius + 25
    circle(radius)