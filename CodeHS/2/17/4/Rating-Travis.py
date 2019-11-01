"""
This code will draw a symbol depending on the rating given. A red x mark will
be drawn if the rating is less than or equal to 4, a yellow line will be drawn
if the rating is in between 5 including 5 and 7 including 7. Else, a check will be
drawn
"""
speed(0)
penup()
pensize(10)
rating=int(input("Rating? (1-10): "))
def draw_x(): ## draws a red "x"
    left(45)
    color("red")
    pendown()
    for i in range(4):
        forward(40)
        backward(40)
        left(90)
def draw_line(): ## draws a yellow line
    pendown()
    color("yellow")
    backward(30)
    forward(60)
def draw_check(): ## draws a green check
    right(45)
    backward(30)
    pendown()
    color("green")
    forward(30)
    left(90)
    forward(60)
## check the rating to determine what symbol to draw
if rating <= 4:
    draw_x()
elif rating >=5 and rating <=7:
    draw_line()
else:
    draw_check()