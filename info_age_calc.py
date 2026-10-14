
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