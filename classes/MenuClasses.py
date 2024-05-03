from classes.UserDatabaseClass import *
from classes.ExpenseDatabaseClass import *
import sys

class BaseMenu():
    """Class that builds a base for various Menus. It instantiates
    and has two methods for rendering the menu and letting the 
    user choose an option from the menu"""

    def __init__(self, items: list):
        self.items = items
        self.selection = None

    def render_menu(self):
        # Render the items as options for the menu
        print('Please select an option:\n')

        for num, option in enumerate(self.items):
            print(f'{num + 1}. {option}')

    def get_user_selection(self):
        """Prompt the user for an option to choose and 
        return the selection""" 
        while True:
            try:
                self.selection = int(input('\nYour selection: '))
                if self.selection not in range(1, len(self.items) + 1):
                    print('Invalid option')
                    continue
                break
            
            except ValueError:
                print('Invalid input please select a number')
                continue


class UserMenu(BaseMenu):
        """UserMenu class inherits from BaseMenu class. This one
        shows the first Usermenu when starting the program. It comes
        with two additional methods. The initialize method which starts
        the whole menu sequence and the method which acts on the user input."""

        def __init__(self, database):
            """Initializing an instance with the userdatabase as a class 
            attribute and the options which the menu will render for the user"""
            self.database = database
            self.user = None
            options = ['select user', 'add user', 'delete user', 'exit program']
            super().__init__(options)

        def initialize(self):
            self.render_menu()
            self.get_user_selection()
            return self.act_on_user_selection()

        def act_on_user_selection(self):
            """Calling respective methods from the Userdatabase class
            to select, add user and delete user from the user databank"""
            match self.selection:
                case 1:
                    # showing our users and let the user choose his name
                    if not self.database.show():
                        print('No users found')
                        return None
                    
                    while True:
                        try:
                            # Let user choose his number and set our user attribute to his username
                            self.user = self.database[int(input('Your number: ')) - 1]  # TO DO negative ints get the values from the end of the list
                            return self.user
                        except (IndexError, ValueError):
                            # Prompt user again if he chooses an invalid option
                            print('Invalid entry try again')
                            continue
                case 2:
                    while True:
                        # Instantiate a new user from the User class
                        new_user = User(input('Your name: '), input('Choose username: '))
                        # Check if the username already exist reprompt if it exists
                        if new_user.__dict__['username'] in (x['username'] for x in self.database):
                            print("Username already taken")
                            continue
                        break
                    self.database.add_user(new_user)
                case 3:
                    # Show the list of users
                    self.database.show()
                    # Delete user by index
                    user_to_delete = self.database[int(input('Your number: ')) - 1]
                    self.database.delete_user(user_to_delete)    
                case 4:
                    sys.exit('Exiting the program...')



class ExpenseMenu(BaseMenu):
    def __init__(self, user, database):
        options = ['Show expense history', 'add expense', 'delete expense', 'return to main menu']
        self.user = user
        self.database = database
        super().__init__(options)

    def initialize(self):
        self.render_menu()
        self.get_user_selection()
        self.act_on_user_selection()
        
    def act_on_user_selection(self):
        match self.selection:
            case 1:
                 if not self.database.show():
                     print('No expenses found')
            case 2:
                # Instantiate a new expense with the data from the user
                while True:
                    new_expense = Expense(input('Amount: '), input('Date: '), input('Category: '))
                    self.database.add_expense(new_expense)
                    if not input('To add more expenses press "enter" to quit press any key: ') == '':
                        break
            case 3:
                # Show the list of expenses
                self.database.show()
                # Delete expense by index
                expense_to_delete = self.database[int(input('Your number: ')) - 1]
                self.database.delete_expense(expense_to_delete)
            case 4:
                return None # Return to main menu