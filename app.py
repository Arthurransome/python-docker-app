import os

def perform_calculation():
    print("Simple Calculator")
    print("Available operations: add, subtract, multiply, divide")
    operation = input("Enter operation: ").strip().lower()

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    result = None
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero.")
            return
    else:
        print("Invalid operation.")
        return

    print(f"Result: {result}")
    log_result(operation, num1, num2, result)

def log_result(operation, num1, num2, result):
    log_file = "calculation_history.txt"
    with open(log_file, "a") as file:
        file.write(f"{num1} {operation} {num2} = {result}\n")
    print(f"Result saved to {log_file}")

if __name__ == "__main__":
    while True:
        perform_calculation()
        if input("Do you want to perform another calculation? (yes/no): ").strip().lower() != "yes":
            break
