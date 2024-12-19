def calculator():
    print("\nCalculator Application")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("\nOperations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    operation = input("Choose an operation (1-4): ")

    if operation == "1":
        print(f"Result: {num1 + num2}")
    elif operation == "2":
        print(f"Result: {num1 - num2}")
    elif operation == "3":
        print(f"Result: {num1 * num2}")
    elif operation == "4":
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero.")
    else:
        print("Invalid operation.")

calculator()