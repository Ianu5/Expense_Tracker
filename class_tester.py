from expense_tracker_classes import User, UserMenu, users


user = User('Ssaja', 'Hur', 'Jesaja')
user2 = User('Dillane', 'Badillo', 'Debvy')

user.save()
user2.save()

for user in users:
    print(user)