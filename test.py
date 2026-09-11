def calculate(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Invalid operator"

while True:
    print("\n--- Calculator ---")
    choice = input("Enter calculation (or 'q' to quit): ")
    
    if choice.lower() == 'q':
        print("Goodbye!")
        break

    try:
        num1 = float(input("First number: "))
        op = input("Operator (+, -, *, /): ")
        num2 = float(input("Second number: "))
        print(f"Result: {calculate(num1, num2, op)}")
    except ValueError:
        print("Please enter valid numbers.")    