# Simple Calculator
# Performs basic arithmetic operations based on user input

def add(a, b):
    return a + b
    pass

def subtract(a, b):
    return a - b
    pass

def multiply(a, b):
    return a * b
    pass

def divide(a, b):
    if b == 0:
        return "Error: division by 0"
    else:
        return a/b
    pass

def main():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator: ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            answer = add(num1, num2)
        elif operator == "-":
            answer = subtract(num1, num2)
        elif operator == "*":
            answer = multiply(num1, num2)
        elif operator == "/":
            answer = divide(num1, num2)
        else:
            answer = "Error: invalid operator"

        print("Answer: ", answer)

    except ValueError:
        print("Invalid number entered.")

if __name__ == "__main__":
    main()
