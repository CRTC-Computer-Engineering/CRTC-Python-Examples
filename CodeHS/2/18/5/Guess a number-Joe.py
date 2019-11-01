lineModifier = 50
secretNum = 4

def green_check():
    pensize(10)
    color("Green")
    left(45)
    for i in range(2):
        forward(lineModifier * 3)
        left(180)
    left(90)
    forward(lineModifier)
    
while int(input("Guess a number between 1 and 10: ")) != secretNum:
    print("Wrong! Try again.")
green_check()