speed(0)
def make_three_circles():
    for i in range(12):
        left(10)
        penup()
        forward(100)
        pendown()
        color("red")
        begin_fill()
        circle(10)
        end_fill()
        penup()
        backward(100)
        
        left(10)
        penup()
        forward(100)
        pendown()
        color("purple")
        begin_fill()
        circle(10)
        end_fill()
        penup()
        backward(100)
        
        left(10)
        penup()
        forward(100)
        pendown()
        color("blue")
        begin_fill()
        circle(10)
        end_fill()
        penup()
        backward(100)
make_three_circles()