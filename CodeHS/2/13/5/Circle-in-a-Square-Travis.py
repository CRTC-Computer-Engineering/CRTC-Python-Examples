speed(0)
penup()
radius=int(input("Choose a radius: "))
def make_circle_in_a_square(radius):
    setposition(0-radius, 0-radius)
    color("red")
    begin_fill()
    for i in range(4):
        pendown()
        forward(radius*2)
        left(90)
    end_fill()
    penup()
    forward(radius)
    color("blue")
    pendown()
    begin_fill()
    circle(radius)
    end_fill()
make_circle_in_a_square(radius)