def calculate_area(side_length = 10):
    print "Side length: " + str(side_length)
    print "The area of a square with sides of length " + str(side_length) + " is " + str(side_length * side_length)

user_length = int(input("Enter side length: "))

if user_length <= 0:
    calculate_area()
else:
    calculate_area(user_length)
