class User:
    """A user class that has the functionality of creating a user for our user database"""
    def __init__(self, username, surname=None, first_name=None):
        self.username = username
        self.surname = surname
        self.first_name = first_name

    def __repr__(self):
        return f'Username: {self.username}'
    
    def __bool__(self):
        return bool(self.username)


class UserMenu:
    """User configuration menu"""
    text = """
    1. Add user
    2. Delete user 
    3. Select user"""

    @classmethod
    def __repr__(cls):
        return cls.text
    

class Expense:
    ...
    def __init__():
        ...

    def __repr__():
        ...
    
