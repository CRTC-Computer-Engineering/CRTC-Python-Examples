"""
This program made by Joe
"""
numerator = int(input("Enter a numerator: "))
denominator = int(input("Enter denominator: "))

while denominator == 0:
    denominator = int(input("Enter denominator: "))



if numerator / denominator * denominator == numerator:
    print "Divides evenly!"
else:
    print "Doesn't divide evenly."