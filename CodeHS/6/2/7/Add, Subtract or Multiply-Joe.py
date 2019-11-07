import operator

def multiply():
    pass
def add():
    pass
def subtract():
    pass

operators = {"add":operator.add, "subtract":operator.sub, "multiply":operator.mul}
symbols = {"add":'+', "subtract":'-', "multiply":'*'}

first_number = int(input("First number: "))
second_number = int(input("Second number: "))
symbol = input("Choose an operation (add, subtract, multiply): ")

ans = operators[symbol](first_number, second_number)


print (str(first_number) + " " + symbols[symbol] + " " + str(second_number) + " = " + str(ans))