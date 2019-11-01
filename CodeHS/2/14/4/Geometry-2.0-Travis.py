speed(0)
penup()
setposition(0,-150)
add=0
radius=20
for i in range(7):
    pendown()
    circle(radius + add, 360, i)
    add = add + 20