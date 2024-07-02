def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calculator():

    print("Welcome to the basic calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide\n")

    userChoice = input("Which option will you be using today (1, 2, 3, 4)")

    if userChoice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter first number: "))

        if userChoice == '1':
            print(f"{num1} + {num2} = {round(add(num1, num2))}")
        
        if userChoice == '2':
            print(f"{num1} - {num2} = {round(subtract(num1, num2))}")
        
        if userChoice == '3':
            print(f"{num1} * {num2} = {round(multiply(num1, num2))}")
        
        if userChoice == '4':
            print(f"{num1} / {num2} = {round(divide(num1, num2))}")

    else:
        print("Invalid Output")



calculator()