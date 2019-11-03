speed(0)
setposition(-200,-200)
def make_square(color_square): ##Creates one square 40x40 pixels with color color_square
    color(color_square)
    begin_fill()
    for i in range(4):
        forward(40)
        left(90)
    end_fill()
def make_row(first_color, second_color): ## creates a row of 10 squares with alternating colors between first_color and second_color
    mod_check=0
    for i in range(10):
        if mod_check%2==0:
            make_square(first_color)
        else:
            make_square(second_color)
        forward(40)
        mod_check=mod_check+1
def up_a_row(): ## moves tracy up a row
    penup()
    backward(400)
    left(90)
    forward(40)
    right(90)
def make_two_rows(): ## makes a row with red,black and a row on top of it with black,red
    make_row("red", "black")
    up_a_row()
    make_row("black", "red")
def make_checkerboard(): ##makes the checker board using make_two_rows and up_a_row
    for i in range(5):
        make_two_rows()
        up_a_row()
make_checkerboard()
    