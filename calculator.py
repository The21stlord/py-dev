import math
while True:
    print("-----calculator-----")
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == "n":
        break
    elif choice.lower() == "y":
        pass
    else:
        print("either y or n sherlock!")
        continue
    def get_float(intake): 
        while True:
            try:
                return float(input(intake))
            except ValueError:
                print("numbers only lil bro!")
    def get_operator(intake):
        while True:
            op = input(intake)
            if op in ["+", "-", "*", "/", "power", "%", "root"]:
                return op
            else:
                print("Invalid operator. Please enter +, -, *, /, power, %, or root.")
    a = get_float("Enter first number: ")
    op = get_operator("Enter operator (+, -, *, /, power, %, root): ")
    b = get_float("Enter second number: ")

    if op == "+":
            result = a + b
            print(f"{a} + {b} = {result}")
    elif op == "-":
            result = a - b
            print(f"{a} - {b} = {result}")
    elif op == "*":
            result = a * b
            print(f"{a} * {b} = {result}")
    elif op == "/":
        while True:
            if b == 0:
                print("Can't do that lil bro")
                b = get_float("Enter second number: ")
            else:
                result = a / b
                print(f"{a} / {b} = {result}")
                break
        if b == 0:
                print("Can't do that lil bro")
                continue
        else:
            result = a / b
            print(f"{a} / {b} = {result}")
    elif op == "power":
            result = math.pow(a, b)
            print(f"{a} ^ {b} = {result}")
            print(math.ceil(result))
            print(math.floor(result))
    elif op == "%":
            result = a % b
            print(f"{a} % {b} = {result}")
            print(math.ceil(result))
            print(math.floor(result))
    elif op == "root":
            result = math.sqrt(a)
            print(f"√{a} = {result}")
            print(math.ceil(result))
            print(math.floor(result))
    else:
            print("Don't be smart boy")
print("bye")