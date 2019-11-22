# Write your function for converting Celsius to Fahrenheit here.
# Make sure to include a comment at the top that says what
# each function does!
def convert_celsius_to_fahrenheit(num):
    return float((num - 32) / 1.8)



# Now write your function for converting Fahrenheit to Celsius.
def convert_fahrenheit_to_celsius(num):
    return float((1.8 * num) + 32)



# Now change 0C to F:
print convert_celsius_to_fahrenheit(0)

# Change 100C to F:
print convert_celsius_to_fahrenheit(100)

# Change 40F to C:
print convert_fahrenheit_to_celsius(40)

# Change 80F to C:
print convert_fahrenheit_to_celsius(80)
