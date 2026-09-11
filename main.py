"""
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
"""
"""
#personal information and age calculator
while True:
    status = input("are you a student? (y/n): ")
    if status.lower() == "y":
        pass
        name = input("whats your name: ")
        age = int(input("whats your age: "))
        age = age + 1
        print(f"Hello {name}, next year you will be {age} years old.")
    elif status.lower() == "n":
        print("feature only available for students")
    break
"""
"""
name = input("whats your name customer: ")
product_name = input("what you wanna buy: ")
product_price = float(input("how much is it: "))
while True:
        has_discount_code = input("do you have a discount code? y/n: ")
        if has_discount_code.lower() == "y":
            discount_code = input("enter your discount code: ")
            if discount_code.upper() == "DISCOUNT10":
                final_price = product_price * 0.7  #applies discount of 30percent
                print(f"Congratulations {name.capitalize()}, you have a 30% discount! Your final price is: ${final_price:.2f}") #the .2f formats the final price to 2 decimal places
            else:
                    print(f"Invalid discount code. No discount applied. \n Your final price is: ${product_price:.2f}")                             
        elif has_discount_code.lower() == "n":
                final_price = product_price
                print(f"Thank you {name.capitalize()}, your final price is: ${final_price:.2f}")
        else:
                print("Please enter 'y' or 'n'.")
                continue
        break
"""
"""
student_name = input("whats your name : ")
math_score = float(input("whats your math score: "))
physics_score = float(input("whats your physics score: "))
english_score = float(input("whats your english score: "))
total = math_score + physics_score + english_score
average = total / 3
if average >= 90:
    grade = "A"
    remarks = "Excellent work!"
if average >= 80 and average < 90:
    grade = "B"
    remarks = "Good job!"
if average >= 70 and average < 80:
    grade = "C"
    remarks = "Keep it up!"
if average >= 60 and average < 70:
    grade = "D"
    remarks = "You can do better!"
if average < 60:
    grade = "F"
    remarks = "You need to improve!"
print(f"\nStudent Name: {student_name}")
print(f"Math Score: {math_score}")
print(f"Physics Score: {physics_score}")
print(f"English Score: {english_score}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
print(f"Remarks: {remarks}")
"""
