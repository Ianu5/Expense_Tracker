users = []

class User:
    """A user class that has the functionality of creating a user for our user database"""
    def __init__(self, username, surname=None, first_name=None):
        self.username = username
        self.surname = surname
        self.first_name = first_name

    def __repr__(self):
        return f"{self.username}"
    
    def __bool__(self):
        return bool(self.username)

    def save(self):
        users.append((self.username, self.first_name, self.surname))

"""Maybe I can build a overarching class called 'Database' which has the
characteristics of a database from which I can defer special cases such as
User database or expense database
What attributes and functions would a database class have to have?
- file initiator
- a way to represent data
- a way to add and delete data
"""
class UserDatabase:
    """A class for our database for storing users"""
    def __init__(self):
        ...


class UserMenu:
    """User configuration menu"""
    text = """
    1. Add user
    2. Delete user 
    3. Select user
    4. Quit
    """

    @classmethod
    def render(cls):
        print(cls.text)

    @classmethod
    def choose_option(cls):
        answer = int(input("Select option: "))
        if answer == 1:
            UserMenu.add_user()
        elif answer == 2:
            UserMenu.delete_user()
        elif answer == 3:
            UserMenu.select_user()
        elif answer == 4:
            print("Quitting program")
        else:
            print("Invalid option")

    @classmethod
    def add_user(cls):
        print("added user")
        return True
    
    @classmethod
    def delete_user(cls):
        print("deleted user")
        return True
    
    @classmethod
    def select_user(cls):
        print("selected user")
        return True
    

class Expense:
    ...
    def __init__():
        ...

    def __repr__():
        ...
    
