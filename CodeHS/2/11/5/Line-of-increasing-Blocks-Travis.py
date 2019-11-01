speed(0)
penup()
setposition(-150,0)
pendown()

def make_square():
    length = 10
    for i in range(5):
        for i in range(4):
            pendown()
            forward(length)
            left(90)
        penup()
        forward(length * 2)
        length = length + 10
make_square()