import sys
import os
import json
import re
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
        
        # If the response is 1 start a loop to prompt the user for expenses
        if response == '1':
        # the user for expenses
            while True:
                # Prompt the user for their expense
                amount = validate_amount()
                category = validate_category()
                date = validate_date()
                expense = Expense(amount, category, date)

                # Add the expense to the list of expenses
                update_expenses(expenses, expense)
                write_expense_to_file(expenses)

                # Ask the user if he wants to continue adding expenses
                prompt = ask_for_continuation()
                if not user_continue(prompt):
                    break
            continue

        # Show history when user chosses 2
        elif response == "2":
            show_history(expenses)
            continue

        # Exit the program if user chooses 3
        elif response == "3":
            print("Exiting the Program...")
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
    return bool(response in valid_input)

def file_exists():
    # Check if a expenses.json file exists 
    return bool(os.path.exists('expenses.json'))

def get_data_from_existing_file():
    # Open expenses file and read data into a list
    with open('expenses.json', 'r') as file:
            expenses = json.load(file)
    return expenses

def validate_amount():
    while True:
        try:
            amount = input("Amount spent: ")
            amount = "{:.2f}".format(float(amount))
            break
        except ValueError:
            print("Invalid Input. Input a digits with maximum two decimals")
            continue
    return amount

def validate_category():
    return input("Reason for spending: ").title()

def validate_date():
    while True:
        date = input("Date of expense: ")
        found_pattern = re.search(r'^\d{4}/\d{2}/\d{2}$', date)
        if found_pattern:
            break
        else:
            print("Input format: YYYY/MM/DD")
            continue
    return date

def update_expenses(expenses, expense):
    # Add data to the expenses list in form of a dictionary
    expenses.append(expense.__dict__)

def write_expense_to_file(expenses):
    # Write the added expense to the expenses file
    with open ('expenses.json', 'w') as file:
        json.dump(expenses, file, indent=2)


def show_history(expenses):
    print('\n--------------------------------------------------------------------------\n'
          '                        Your expenses\n')
    # Print out all expenses the user added in a better format
    for expense in expenses:
        for key, value in expense.items():
            print(f'{key.title()}: {value} ', end='')
        print()

def ask_for_continuation():
    question = "Do you want add another expense?"
    question += " (To continue press 'Enter'"
    question += " | To exit enter any key): "
    return input(question)

def user_continue(user_input):
    # return true if user inputs nothing and false if he enters any key
    return bool(user_input == '')

if __name__ == "__main__":
    main()