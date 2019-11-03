speed(0)
radius = 25
count = 1
row_value = int(input("How many circles (1-8) would you like on the bottom? "))
x_value = -((row_value*(radius*2))/2)+25
y_value = -225 + (count*radius)
def moveup():
    setposition(x_value,y_value)
penup()
moveup()
def draw_row():
    for i in range(row_value):
        pendown()
        circle(radius)
        penup()
        forward(radius*2)
for i in range(row_value):
    draw_row()
    count = count + 1
    y_value = -225 + ((count*radius)*2)-25
    x_value = -((row_value*(radius*2))/2)+50
    moveup()
    row_value=row_value-1