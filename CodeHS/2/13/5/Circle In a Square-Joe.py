circleColor = "Blue" # Set color of the circle
squareColor = "Red" # Set color of the square

def circle_in_square(radius): # Pass radius to the def
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
    end_fill() # Finish Square
    begin_fill() # Start Circle
    print("Drawing Circle with radius " + str(radius))
    color(circleColor)
    circle(radius)
    end_fill()
    
circle_in_square(input("Shape Size: ")) # Ask for user input