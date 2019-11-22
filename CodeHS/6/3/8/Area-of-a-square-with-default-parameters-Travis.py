def calculate_area(side_length = 10):
    print side_length
    print side_length * side_length

user_length = int(input("Enter side length: "))

if user_length <= 0:
    calculate_area()
else:
    calculate_area(user_length)
