# Python calculator

import math

while True:
    while True:
        operator = input("Please enter an operator (+ - * / sqrt pow): ")
        if operator in ["+", "-", "*", "/", "sqrt", "pow"]:
            break
        print(f"{operator} is invalid. Please try again.")

    while True:
        try:
            num1 = float(input("Please enter the 1st number: "))
            if operator != "sqrt":
                num2 = float(input("Please enter the 2nd number: ")) # If it's sqrt or pow then 2nd number is "to the power of" same for sqrt
            break
        except ValueError:
            print("Enter a valid number.")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error, you cannot divide by zero.")
            continue
        result = num1 / num2
    elif operator == "sqrt":
        if num1 < 0:
            print("Negative numbers are not allowed in a square root.")
            continue
        result = math.sqrt(num1)
    elif operator == "pow":
        result = math.pow(num1, num2)

    print(f"The result is {result}")

    again = input("Would you like to calculate again? (Y/N): ") # Loops back to the beginning of the code
    if again.upper() == "N":
        break