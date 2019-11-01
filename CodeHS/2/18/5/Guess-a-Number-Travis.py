speed(0)
secret_number = 5
def draw_check(): ##Draws the green check mark
    right(45)
    color("green")
    pensize(10)
    backward(50)
    forward(50)
    left(90)
    forward(100)
while int(input("Give a number (1-10): ")) != secret_number: ## Do not save the input as user_input. codehs crashed
    print("Try again")
draw_check()