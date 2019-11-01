numCircles = 8
circleSize = 20

speed(0)
def make_caterpillar_cell(color_choice, m_size):
    pendown()
    begin_fill()
    color(color_choice)
    circle(m_size)
    end_fill()
    penup()
    advance_to_next(m_size)
    
def advance_to_next(m_size):
    penup()
    forward(m_size * 2)
    
penup()
setposition(-100, 0)
for i in range(numCircles):
    make_caterpillar_cell(input("Color for cell " + str(i + 1) + ": "), circleSize)