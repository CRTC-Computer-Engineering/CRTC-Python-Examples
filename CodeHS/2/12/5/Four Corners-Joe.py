def drawCube(side_len):
    pendown()
    for i in range(16): # 16 beacuse codehs is dumb
        forward(side_len)
        left(90)
    penup()
    
penup()
setposition(-200, -200)
for i in range(4):
    square_length = input("Enter square size: ")
    drawCube(square_length)
    forward(400)
    left(90)
print("Done!")  