import sys
import os
import json
from classes import Expense

def main():

    if file_exists():
        # If a file with prior expenses exist read this data into a list
        expenses = get_data_from_existing_file()
    else:
        # If the file does not exist initialize an empty list
        expenses = []


    while True:
        # Get a response from user
        response = get_response_for_menu()

        # Begin the loop anew when user does not give a valid response
        if not viable_user_input(response):
            print(f"{response} is not a viable option. Choose 1-3")
            continue

        # When the user chooses 1 add an expense
        if response == "1":
            # Prompt the user for their expense
            expense = get_expense()
            # Add the expense to the list of expenses
            update_expenses(expenses, expense)
            write_expense_to_file(expenses)

        # Show history when user chosses 2
        elif response == "2":
            show_history(expenses)

        # Exit the program if user chooses 3
        elif response == "3":
            print("Exiting the Program")
            break

        # Find out if the user wants to continue
        user_input = ask_for_continuation()
        if user_continue(user_input):
            continue
        else:
            break

def get_response_for_menu():
    # Render a menu for the user to choose from
    print("""
---------------------------- 
|           Menu           |
----------------------------
|                          |
|  1. Add an expense       |
|  2. Show expense history |
|  3. Quit                 |
|__________________________|
           """)
    return input("Your choice: ")
    
def viable_user_input(response):
    # Check if the user chose a viable option
    # Converting the string response to integer
    try:
        response = int(response)
    except ValueError:
        return False
    
    valid_input = [1, 2, 3]
    if response in valid_input:
        return True
    else:
        return False

def file_exists():
    # Check if a expenses.json file exists 
    if os.path.exists('expenses.json'):
        return True
    else:
        return False

def get_data_from_existing_file():
    # Open expenses file and read data into a list
    with open('expenses.json', 'r') as file:
            expenses = json.load(file)
    return expenses

def get_expense():
    # Prompt the user for the spending, date and category of spending
    amount = "{:2f}".format(float(input("Amount spent: ")))
    category = input("Reason for spending: ").title()
    date = input("Date of expense: ")
    expense = Expense(amount, category, date)
    return expense

def update_expenses(expenses, expense):
    # Add data to the expenses list
    expenses.append(expense.__dict__)

def write_expense_to_file(expenses):
    with open ('expenses.json', 'w') as file:
        json.dump(expenses, file, indent=2)


def show_history(expenses):
    print("\n---------------------------\n    Your expenses\n")
    for expense in expenses:
        print(f"""
    date: {expense['date']}
    amount: {expense['amount']}
    category: {expense['category']}
    """)
    print("---------------------------")

def ask_for_continuation():
    question = "Do you want to continue?"
    question += " (Continue: (yes/y)"
    question += " | Exit: (any key)) "
    return input(question)

def user_continue(user_input):
    if user_input.lower() in ['yes', 'y']:
        return True
    else:
        print("Exiting the program...")
        return False
    

if __name__ == "__main__":
    main()