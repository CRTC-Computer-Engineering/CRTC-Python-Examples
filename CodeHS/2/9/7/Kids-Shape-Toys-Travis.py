"""
This code will create 4 different shapes with different colors
"""
penup()
speed(0)
## Creates a green pentagon
def green_shape():
    color("green")
    begin_fill()
    circle(60,360,5)
    end_fill()
## Creates a blue circle
def blue_shape():
    color("blue")
    begin_fill()
    circle(60)
    end_fill()
## Creates a red diamond
def red_shape():
    color("red")
    begin_fill()
    circle(60,360,4)
    end_fill()
## Creates a yellow half circle
def yellow_shape():
    color("yellow")
    begin_fill()
    circle(60,180)
    end_fill()
setposition(100, -150)
pendown()
green_shape()
penup()
setposition(100, 50)
pendown()
blue_shape()
penup()
setposition(-100, 50)
pendown()
red_shape()
penup()
setposition(-100, -150)
pendown()
yellow_shape()
penup()