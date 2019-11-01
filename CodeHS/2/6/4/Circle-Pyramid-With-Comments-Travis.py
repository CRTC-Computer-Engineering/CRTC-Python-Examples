penup()
setposition(-100, -200)
## Makes the bottom three circles.
for i in range(3):
    pendown()
    circle(50)
    penup()
    forward(100)
setposition(-50, -100)
## Makes the middle two circles.
for i in range(2):
    pendown()
    circle(50)
    penup()
    forward(100)
"""
Makes the last circle.
"""
setposition(0, 0)
pendown()
circle(50)
penup()
forward(100)