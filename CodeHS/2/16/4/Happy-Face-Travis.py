speed(0)
penup()

happy=input("Are you happy? (yes,no): ")

def make_eye():
    color("black")
    pendown()
    begin_fill()
    circle(20)
    end_fill()
    penup()

def make_smiley():
    ##FACE
    setposition(0,-100)
    color("yellow")
    pendown()
    begin_fill()
    circle(100)
    end_fill()
    penup()
    
    ##MOUTH
    setposition(0,-70)
    pensize(10)
    color("black")
    pendown()
    circle(60,90)
    color("yellow")
    circle(60,180)
    color("black")
    circle(60,90)
    penup()
    
    ##EYES
    setposition(-30,25)
    make_eye()
    forward(70)
    make_eye()
    
    

if happy == "yes":
    make_smiley()