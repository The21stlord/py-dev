import random
import string
while True: 
    print("welcome to the random password generator")
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == "n":
        break
    elif choice.lower() == "y":
        pass
    else:
        print("either y or n sherlock!")
        continue
   
    def yes_or_no(prompt):
        while True:
            response = input(prompt + " (y/n): ").strip().lower()
            if response in ['y', 'n']:
                return response == 'y'
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
    def choose_characters():
        rdm_pool = {(string.ascii_lowercase, yes_or_no("Include lowercase letters?")),
                    (string.ascii_uppercase, yes_or_no("Include uppercase letters?")),
                    (string.digits, yes_or_no("Include digits?")),
                    (string.punctuation, yes_or_no("Include punctuation?"))}
        characters = ""
        for char_set, include in rdm_pool:
            if include:
                characters += char_set
        return characters
            

    def generate_password(length, characters):
        password = ""
        password = "".join(random.choice(characters) for _ in range(length))
        return password

    while True:

        try:
            characters = choose_characters()
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")


    password = generate_password(length, characters)
    print(f"Generated password: {password}")
print("Thank you for using the random password generator!")