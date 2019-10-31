"""
This program made by Joe
"""
shapeSize = 60

def draw_polygon(m_sides, m_color, m_size):
    pendown()
    begin_fill()
    color(m_color)
    circle(m_size, 360, m_sides)
    end_fill()
    penup()

def draw_circle(m_angle, m_color, m_size):
    pendown()
    begin_fill()
    color(m_color)
    if (m_angle != 360):
        circle(m_size, m_angle)
    else:
        circle(m_size)
    end_fill()
    penup()

penup()
setposition(100, (-100 - shapeSize))
draw_polygon(5, "green", shapeSize)
setposition(-100, (100 - shapeSize))
draw_polygon(4, "red", shapeSize)
setposition(100, (100 - shapeSize))
draw_circle(360, "blue", shapeSize)
setposition(-100, (-100 - shapeSize))
draw_circle(180, "yellow", shapeSize)
color("black")
setposition(0, 0)