"""
This program made by Joe
"""
def startDraw(requestedColor):
    pendown()
    color(requestedColor)
    begin_fill()

def stopDraw():
    end_fill()
    penup()

def drawSmile(happy, headcolor, headsize):
    eyeHeight = headsize * 1.5
    
    startDraw(headcolor)
    circle(headsize)
    stopDraw()
    forward(headsize * 0.6)
    left(90)
    forward(eyeHeight)
    left(90)
    for i in range(2):
        forward(headsize * 0.3)
        startDraw("Black")
        circle(headsize * 0.1)
        stopDraw()
        forward(headsize * 0.3)
    left(90)
    forward(eyeHeight)
    left(90)
    forward(headsize * 0.6)
    
    if (happy == "happy"):
        left(90)
        forward(headsize * 0.8)
        left(90)
        forward(headsize * 0.5)
        left(90)
        startDraw("Black")
        circle(headsize * 0.5, 180)
        left(90)
        forward((headsize * 0.5) * 2)
        stopDraw()
    elif (happy == "sad"):
        left(90)
        forward(headsize * 0.4)
        right(90)
        forward(headsize * 0.5)
        left(90)
        startDraw("Black")
        circle(headsize * 0.5, 180)
        left(90)
        forward((headsize * 0.5) * 2)
        stopDraw()
    else:
        print("Error in input, expected 'happy' or 'sad'")
        print(happy)

drawSmile(input("Input your mood, supported inputs are: happy and sad:"), "Yellow", 80)