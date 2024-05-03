from classes.MenuClasses import *
from classes.UserDatabaseClass import *
from classes.ExpenseDatabaseClass import *

userData = UserDatabase('./files/users.json')

def main():
    while True:
        usermenu = UserMenu(userData)
        user = usermenu.initialize()
        if user:
            expense_database = ExpenseDatabase(user)
            expense_menu = ExpenseMenu(user, expense_database)
            expense_menu.initialize()


    
if __name__ == "__main__":
    main()