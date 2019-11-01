"""
This program made by Joe
"""
snowman_list = []

def draw_snowman(m_inputs):
    for current_ball in m_inputs:
        pendown()
        color("grey")
        begin_fill()
        circle(int(current_ball))
        end_fill()
        penup()
        left(90)
        forward(2 * int(current_ball))
        right(90)

def draw_sequential_snowman(m_input):
    for i in range(3):
        pendown()
        color("grey")
        begin_fill()
        circle(m_input)
        m_input = m_input / 2
        end_fill()
        penup()
        left(90)
        forward(4 * int(m_input))
        right(90)
    
penup()
setposition(0,-200)
for i in range(3):
    user_input = input("Size for ball " + str(i + 1) + ": ")
    snowman_list.append(user_input)
#draw_snowman(snowman_list)
draw_sequential_snowman(100)