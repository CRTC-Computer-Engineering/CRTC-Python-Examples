speed(0)
secret_number = 5
user_input = int(input("Give a number (1-10): "))
def draw_check(): ##Draws the green check mark
    right(45)
    color("green")
    pensize(10)
    backward(50)
    forward(50)
    left(90)
    forward(100)
while user_input != secret_number: ## Do not save the input as user_input. codehs crashed
    if user_input < secret_number: ## CodeHS compiler broke. 
        print("guess higher!")
    else:
        print("guess lower!")
draw_check()