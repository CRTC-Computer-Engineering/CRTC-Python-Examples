circleColor = "Blue"
squareColor = "Red"

def circle_in_square(radius):
    pendown()
    begin_fill()
    color(squareColor)
    forward(radius)
    for i in range(3):
        left(90)
        forward(int(radius) * 2)
        print("Drawing square with radius " + str(int(radius * 2)))
    left(90)
    forward(radius)
    end_fill()
    begin_fill()
    print("Drawing Circle with radius " + str(radius))
    color(circleColor)
    circle(radius)
    end_fill()
    
circle_in_square(input("Shape Size: "))