"""
This program made by Joe
"""
minSquareSize = 50
growthFactor = 50
maxSquareSize = 350

def fillSquares():
    length = minSquareSize
    while length <= 350:
        drawSquare(length)
        length = length + growthFactor

def drawSquare(length):
    penup()
    setposition(0,0)
    right(90)
    forward(length / 2)
    left(90)
    forward(length / 2)
    pendown()
    for i in range(4):
        left(90)
        forward(length)

fillSquares()