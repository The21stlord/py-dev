from datetime import date, datetime
now = date.today()
timestamp = now.strftime("%Y-%m-%d")
def expense_add(expense_name, expense_amount, timestamp):
    with open("expenses.txt", "a") as file:
        file.write(f"{expense_name}: {expense_amount}, {timestamp}\n")
while True:
    print ("=======Expense Tracker=======")
    print ("\n1. Add Expense\n2. View Expenses\n3. Calculate Total\n4. Find Expense\n5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        expense_name = input("Enter expense name: ")
        expense_amount = float(input("Enter expense amount: "))
        expense_add(expense_name, expense_amount, timestamp)
    if choice == '2':
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()
            for expense in expenses:
                print(expense.strip())
    if choice == '3':
        total = 0
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()
            for expense in expenses:
                amount = float(expense.split(":")[1].split(",")[0].strip())
                total += amount
        print(f"Total Expenses: {total}")
    if choice == '4':
        search_name = input("Enter expense name to find: ")
        found = False
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()
            for expense in expenses:
                if search_name.lower() in expense.lower():
                    print(expense.strip())
                    found = True
        if not found:
            print("Expense not found.")
    if choice == '5':
        print("Exiting Expense Tracker.")
        break
    