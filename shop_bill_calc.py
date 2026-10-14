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