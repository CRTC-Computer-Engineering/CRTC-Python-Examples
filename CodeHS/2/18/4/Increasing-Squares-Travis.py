speed(0)
penup()
length=0
def move_to_position():
    penup()
    backward(25)
    right(90)
    forward(25)
    left(90)
def make_square():
    pendown()
    for i in range(4):
        forward(length)
        left(90)
    penup()
while length < 400:
    penup()
    make_square()
    move_to_position()
    length = length + 50
