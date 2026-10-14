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