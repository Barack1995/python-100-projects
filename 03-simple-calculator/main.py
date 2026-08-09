def simple_calculator(num1,num2, operation):
        if operation == '+':
            total = num1 + num2
            return total
        elif operation == "-":
            difference = num1 - num2
            return difference
        elif operation =="*":
            product = num1 * num2
            return product
        elif operation == "/":
            if num2 ==0:
                return None
            else:
                quotient = num1 / num2
                return quotient


while True:
    try:
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        operation = input("Enter operation (+, -,*,/): ")
        if operation not in ['+', '-', '*', '/']:
            print("Error: Invalid operation. Please enter one of +, -, *, /.")
            continue
        result = simple_calculator(num1, num2, operation)
        if result is None:
            print("Error: Division by zero is not allowed.")
        else:
            print("Result:", round(result, 2))
            break
    except ValueError:
        print("Error: Please enter valid integers.")
