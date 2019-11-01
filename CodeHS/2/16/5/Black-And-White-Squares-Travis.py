speed(0)
penup()
backward(120)

sqr_size=30
def black_and_white_squares():
    accum=0
    for i in range(3):
        if accum%2==0:
            make_black_square()
            forward_buffer()
        make_white_square()
        forward_buffer()
        accum=accum+2
def make_white_square():
    for i in range(4):
        pendown()
        forward(sqr_size)
        left(90)
def make_black_square():
    begin_fill()
    for i in range(4):
        pendown()
        forward(sqr_size)
        left(90)
    end_fill()
def forward_buffer():
    penup()
    forward(sqr_size+10)
    pendown()
black_and_white_squares()