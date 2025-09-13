# Simple Calculator
# Performs basic arithmetic operations based on user input

def add(a, b):
    # TODO: Return sum of a and b
    pass

def subtract(a, b):
    # TODO: Return difference of a and b
    pass

def multiply(a, b):
    # TODO: Return product of a and b
    pass

def divide(a, b):
    # TODO: Return quotient of a and b
    # Handle division by zero
    pass

def main():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator: ")
        num2 = float(input("Enter second number: "))

        # Match the operator with the correct function

    except ValueError:
        print("Invalid number entered.")

if __name__ == "__main__":
    main()
