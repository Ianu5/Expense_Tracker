class Expense:
    '''This class represents an Expense'''
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

    def __repr__(self):
        return f'Expense: {self.amount!r} Date: {self.date!r} Category: {self.category!r}'