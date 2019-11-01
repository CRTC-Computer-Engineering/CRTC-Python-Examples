startingRadius = (25 * 4)
radiusGrowth = 25

def draw_concentric_circles(m_radius, m_growth):
    penup()
    right(90)
    forward(startingRadius)
    left(90)
    for i in range(4):
        pendown()
        begin_fill()
        color_choice = input("Choose a color for circle " + str(i) + ": ")
        color(color_choice)
        circle(startingRadius - (radiusGrowth * i))
        end_fill()
        penup()
        left(90)
        forward(radiusGrowth)
        right(90)
        
draw_concentric_circles(startingRadius, radiusGrowth)