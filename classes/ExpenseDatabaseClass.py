import json
from json.decoder import JSONDecodeError
import os



class Expense:
    def __init__(self, amount, date, category=None):
        self.amount = amount
        self.date = date
        self.category = category

    
class ExpenseDatabase:
    """Class that handles our json file for user storage
    it comes with 2 methods save and load to save new users and load
    existing users into memory"""
    def __init__(self, user):
        if user:
            # create a filepath for the user
            self.filepath = f'./files/{user['username']}-expenses.json'
            # If it is the first time for the user to use this program initialize a file
            if not os.path.exists(self.filepath):
                with open(self.filepath, 'w'):
                    pass

            # Load the data from the file to memory
            try:
                self.data = json.load(open(self.filepath, 'r'))
            except JSONDecodeError:
                self.data = []

    def add_expense(self, expense):
        """Append new data to data and save the data to the file"""
        self.data.append(expense.__dict__)

        with open(self.filepath, 'w') as fp:
            json.dump(self.data, fp)

    def delete_expense(self, expense):
        self.data.remove(expense)
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
            print(f'{num + 1}. amount: {item['amount']} date: {item['date']} category: {item['category']}')
        return True