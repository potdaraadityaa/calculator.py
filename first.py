#calculator using python
def multiply(x,y):
    return x * y

def substract(x,y):
    return x - y

def add(x,y):
    return x + y


def divide(x,y):
    if y == 0:
        return "can't divide by zero"
    return x / y

# Calculator Loop
while True:
    print("Option:")
    print("Enter 'addition' to calculate addition")
    print("Enter 'substract' to calculate substraction")
    print("Enter 'multiply' to calculate multiplication")
    print("Enter 'divide' to calculate division")
    print("Enter 'exit' to end the program")

    input = input(": ")

    if input == "exit":
       break
    elif input in ("add", "subtract", "multiply", "divide"):
        a = float(input("Enter first number - "))
        b = float(input("Enter second number - "))

        if input == "add":
            print("Result:", add(a, b))
        elif input == "subtract":
            print("Result:", substract(a, b))
        elif input == "multiply":
            print("Result:", multiply(a, b))
        elif input == "divide":
            print("Result:", divide(a, b))
    else: 
        print("Invalid input")
