import sys
import os
import json
from classes import Expense

def main():

    if os.path.exists('expenses.json'):
        expenses = get_data_from_existing_file()
    else:
        expenses = []


    while True:
        show_menu()

        response = input("Your choice: ")
        if response == "1":
            amount = input("Amount spent: ")
            category = input("Reason for spending: ")
            date = input("Date of expense: ")
            expense = Expense(amount, category, date)
            expenses.append(expense.__dict__)

        if response == "2":
            print("\n-----------------------\nYour expenses\n")
            for expense in expenses:
                print(f"date: {expense["date"]}\namount: {expense["amount"]}\n")
            print("-----------------------")
                
        if response == "3":
            with open ('expenses.json', 'w') as file:
                json.dump(expenses, file, indent=2)
            break



def show_menu():
    print("""
1. Add an expense
2. Show expense history
3. Quit
            """)
    
def get_data_from_existing_file():
    with open('expenses.json', 'r') as file:
            expenses = json.load(file)
    return expenses
    

if __name__ == "__main__":
    main()