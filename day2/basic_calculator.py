"""
Purpose: Basic calculator using user input
"""

try:
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    print(f"The sum of {first_number} and {second_number} is: {first_number + second_number}")
    print(f"The difference is: {first_number - second_number}")
    print(f"The product is: {first_number * second_number}")
    print(f"The quotient is: {first_number / second_number}")


except ValueError:
    print("Error: Please enter valid numbers.")
    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
