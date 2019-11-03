speed(0)
def make_half_bracelet():
    for i in range(18):
        left(10)
        penup()
        forward(100)
        pendown()
        circle(10)
        penup()
        backward(100)
for i in range(2):
    make_half_bracelet()