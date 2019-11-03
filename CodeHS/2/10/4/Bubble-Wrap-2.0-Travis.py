"""
This code will fill the canvas with light blue circles with a white highlight
"""
speed(0)
## This function will draw one row of 10 circles
def draw_circle_row():
    for i in range(10):
        pendown()
        begin_fill()
        color("light blue")
        circle(20)
        end_fill()
        penup()
        forward(40)
## This function will move Tracy from end of row up to beginning of the row on top        
def move_up_a_row():
    left(90)
    forward(40)
    right(90)
    backward(400)
## This creates a white highlight in the top right blue circle
def make_highlight():
    for i in range(10):
        pendown()
        color("light blue")
        circle(10,90)
        color("white")
        circle(10,90)
        color("light blue")
        circle(10,180)
        penup()
        forward(40)
## Send Tracy to starting position in bottom left corner
penup()
setposition(-180,-200)
# Call circle drawing function 10 times to fill ten rows
for i in range(10):
    draw_circle_row()
    move_up_a_row()
## Create the highlights
penup()
setposition(-180, -190)
for i in range(10):
    make_highlight()
    move_up_a_row()