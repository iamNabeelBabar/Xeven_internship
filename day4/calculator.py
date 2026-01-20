# Multi-Operation Calculator with Type Conversion and Error Handling

def calculator():
    try:
        # Take input from user
        num1 = float(input("Enter the first numbe: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose operation (+, -, *, /, %, **): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
            
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
            
        elif operation == '%':
            if num2 == 0:
                print("Error: Modlus by zero is not allowed.")
                return
            result = num1 % num2
        elif operation == '**':
            result = num1 ** num2
        else:
            print("Invalid operation selected.")
            return

        print(f"{num1} {operation} {num2} = {result:.2f}")

    except ValueError:
        print("Invalid input: Please enter numeric values only.")

calculator()
