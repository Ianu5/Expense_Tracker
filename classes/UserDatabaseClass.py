import json
from json.decoder import JSONDecodeError
from classes.ExpenseDatabaseClass import *
import os

class User:
    """A simple class that represents a user"""
    def __init__(self, name, username):
        self.name = name
        self.username = username
        
    
class UserDatabase:
    """Class that handles our json file for user storage
    The class has 2 attributes. The filepath and the data from file"""
    def __init__(self, filepath):
        self.filepath = filepath
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w'):
                pass
            
        try:
            self.data = json.load(open(self.filepath, 'r'))
        except JSONDecodeError:
            self.data = []

    def add_user(self, user):
        """Add the new user into the list and save the updated list 
        to the file"""
        self.data.append(user.__dict__)
        with open(self.filepath, 'w') as fp:
            json.dump(self.data, fp)

    def delete_user(self, user):
        self.data.remove(user)
        with open(self.filepath, 'w') as fp:
            json.dump(self.data, fp)
            
    def __contains__(self, item):
        """Using special method to check for membership in user database"""
        return item in self.data

    def __getitem__(self, position):
        """Implementing a getitem method to support retrieval and iteration"""
        return self.data[position]
    
    def show(self):
        """Show the contents of the database in a nice way"""
        if len(self.data) == 0:
            return False
        for num, item in enumerate(self.data):
            print(f'{num + 1}. Username: {item['username']}')
        return True