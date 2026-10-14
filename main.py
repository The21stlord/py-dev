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
'''
import random as rdm
print("-----Random Number Generator-----")
while True:
        quit_game = False
        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() == "n":
            break
        elif choice.lower() == "y":
            pass
        else:
            print("either y or n sherlock!")
            continue
        def get_int(intake): 
                while True:
                    try:
                        return int(input(intake))
                    except ValueError:
                        print("numbers only lil bro!")
        def get_guess():
              user_input = input("enter yer guess (or type 'Quit'): ")

              if user_input.lower() == "quit":
                    return "quit"

              try:
                    return int(user_input)
              except ValueError:
                    return None
        while True:
                    lower_bound = get_int("Enter the lower bound: ")
                    upper_bound = get_int("Enter the upper bound: ")
                    if lower_bound > upper_bound:
                            print("Lower bound cannot be greater than upper bound. Please try again.")
                            continue
                    if lower_bound == upper_bound:
                            print("Lower bound cannot be equal to upper bound. Please try again.")
                            continue
                    random_number = rdm.randint(lower_bound, upper_bound)
                    while True:
                        guess = get_guess()
                        if guess == "quit":
                            print(f"youve quit sucker! the answer wuz {random_number}")
                            quit_game = True
                            break
                        elif guess is None: 
                            print("enter a number or type 'quit' lil bro")
                            continue
                        elif guess > random_number:
                              print("yer guess is too high try again")
                              continue
                        elif guess < random_number:
                              print("yer guess is too low try again")
                              continue
                        elif guess == random_number:
                            print("you got it right wasnt expecting that!")
                            quit_game = True
                            break
                        elif quit_game:
                              break
                    if quit_game:
                        break
print("bye")
'''
'''
names = []
while True:
        name = input("enter some names (or 'quit' to... quit): ").strip()

        if name == "quit":
            break
        names.append(name)
for name in names:
    print (f"original: {name}\nUppercase: {name.upper()}\nCapitalized: {name.capitalize()}\nlenght: {len(name)}")
'''
'''
import random

questions = [
    ("whats the capital of france?", "Paris"),
    ("who's the GOAT in football?", "Ronaldo"),
    ("who is the richest man on earth", "Elon Musk"),
    ("whats the hardest substance on earth", "Diamond"),
    ("best phone brand? ", "Samsung"),
    ]
random.shuffle(questions)
score = 0

for question, correct_answer in questions:
    collected_answer = input(question + ": ").strip()
    if collected_answer == "":
        print("youve skipped that one")
        continue
    if collected_answer.lower() == "quit":
        print("youve quit!")
        break
    if collected_answer.lower() == correct_answer.lower():
        print("thats correct!")
        score += 1
    else:
        print(f"as expected from you, wrong again tsk tsk tsk, the answer was {correct_answer}")
print(f"final score is {score} out of {len(questions)}")
'''

# user_0 = {
#     'username': 'enrico',
#     'first': 'efermi',
#     'last': 'fermi'
# }

# for key in user_0.keys():
#     print(f"key: {key}")

favourite_langs = {
    'luke': 'danish',
    'james': 'arabic',
    'tola': 'english',
}
friends = ['james',]
for name in favourite_langs.keys():
    print(f"hi {name}")

    if name in friends:
        lang = favourite_langs[name].title()
        print(f"\t{name.title()}, i see you like {lang}!")
