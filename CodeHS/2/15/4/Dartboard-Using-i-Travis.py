speed(0)
radius = 25
circle(radius)
for i in range(3):
    penup()
    right(90)
    forward(25)
    left(90)
    pendown()
    radius = radius + 25
    circle(radius)