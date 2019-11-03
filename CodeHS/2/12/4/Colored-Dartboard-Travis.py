"""
Draws 4 circles
"""
speed(0)
radius = 125
penup()
right(90)
forward(100)
left(90)
for i in range(4): ## Draws a circle with radius and color_choice color. repeats 4 times
    pendown()
    radius = radius - 25
    color_choice = input("Color of the circle?: ")
    color(color_choice)
    begin_fill()
    circle(radius)
    end_fill()
    penup()
    left(90)
    forward(25)
    right(90)