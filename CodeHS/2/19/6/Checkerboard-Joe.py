"""
This program made by Joe
"""
square_width = 40

speed(0)
def drawModCube(cube_id):
    pendown()
    if (cube_id % 2 == 0):
        color("Red")
    else:
        color("Black")
    begin_fill()
    for i in range(4):
        forward(square_width)
        left(90)
    end_fill()
    penup()
    forward(square_width)
    
penup()
setposition(-200,-200)
for colum in range((400 / square_width)):
    for row in range((400 / square_width)):
        drawModCube(row + colum)
    setposition(-200,-200)
    left(90)
    forward(square_width * (colum + 1))
    right(90)