"""
This program made by Joe
"""
numSquares = 6
squareSize = 20

def doSquares():
    for square in range(numSquares):
        if (square % 2 == 0):
            begin_fill()
        for i in range(4):
            forward(squareSize)
            left(90)
        end_fill()
        penup()
        forward(20 + squareSize)
        pendown()

doSquares()