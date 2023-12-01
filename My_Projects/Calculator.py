#I wanted to try making a calculator using python

#Creating a simple Python calculator taught me the fundamentals of user input handling, basic arithmetic operations, and the structure of modular functions. This project emphasized the importance of error handling for user input validation, ensuring the program handles unexpected inputs gracefully. Moving forward, these skills can be applied to more complex projects, helping me build robust interactive applications, improve user experiences, and enhance my proficiency in writing modular and maintainable code.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

while True:
    # User input for operation and numbers
    operation = input("Choose operation (+, -, *, /) or 'exit' to quit: ")
    
    if operation.lower() == 'exit':
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue

    # Perform the selected operation
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        print("Invalid operation. Please choose +, -, *, or /.")
        continue

    # Display the result
    print("Result:", result)
