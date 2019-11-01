speed(0)
penup()
pensize(10)
happy=input("Are you happy? (yes,no): ")
## Make a smile based on 0,0
def make_smile():
    setposition(0,-70)
    color("black")
    pendown()
    circle(60,90)
    color("yellow")
    circle(60,180)
    color("black")
    circle(60,90)
    penup()
## Make a frown based on 0,0
def make_frown():
    penup()
    setposition(0,-120)
    circle(60,90)
    color("black")
    pendown()
    circle(60,180)
    penup()
## Makes a circle and fills it
def make_eye():
    color("black")
    pendown()
    begin_fill()
    circle(20)
    end_fill()
    penup()
## navigation
setposition(0,-100)
color("yellow")
pendown()
begin_fill()
circle(100)
end_fill()
penup()
## Code branches to see if `happy` or `sad`
if happy == "yes":
    make_smile()
elif happy == "no":
    make_frown()
    penup()
    setposition(0,0)
    left(90)
## Final Navigation
setposition(-30,25)
make_eye()
forward(70)
make_eye()