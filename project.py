import sys
import os
import re
import json
from function import *
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


if __name__ == "__main__":
    main()