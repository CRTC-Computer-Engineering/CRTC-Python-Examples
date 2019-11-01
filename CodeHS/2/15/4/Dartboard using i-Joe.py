"""
This program made by Joe
"""
startingRadius = 25
radiusGrowth = 25

def draw_concentric_circles(m_radius, m_growth):
    for i in range(4):
        circle(m_radius + (m_growth * i))
        right(90)
        penup()
        forward(m_growth)
        pendown()
        left(90)
        
draw_concentric_circles(startingRadius, radiusGrowth)