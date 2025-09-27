def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose operation (add, subtract, multiply, divide): ").strip().lower()

        result = perform_operation(num1, num2, operation)

        if isinstance(result, str) and result.startswith("Error"):
            print(f"Operation failed: {result}")
        else:
            print(f"The result of {operation} is: {result}")

    except ValueError as ve:
        print(f"Invalid input: {ve}")

def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

if __name__ == "__main__":
    main()
