# Expense Tracker
---
####
This Python program tracks the expenses of the user and saves them in a local file.

We start the program with the command: python project.py

The program starts by rendering a simple menu system where the user can choose from.

Let's explore the program further.

In the main part of the program we first check if the user is a recurring user by looking for a
file with previous expenses of the user. If the program finds a file it loads the existing data into a
list of dictionaries. If the program does not find a file it initializes a list.

Next we start a while loop for rendering the menu. I chose to do this, to easily repromt the user and
display the menu again and again until the user decides to exit the program. This saves the user the need to restart the program if he wants to add more expenses or show the expenses he has made.

The user has 3 options to choose from.

1. Adding an expense
2. Show the history of his expenses
3. Exiting the program

This part of the program is mostly run by 2 functions.

A function that renders the menu and prompts the user for a response. And a function that checks if the response is a viable one.

After checking the users input the program checks which option the user chose. 

##### Adding Expense:
The biggest part of the program happens in this part of the program. We ask the user for the amount spent, why and when he spent the money. The program validates the users input and creates an instance of a costom class (Expense). This instance is then used to update the list with prior expenses and written to the local file where the data is stored.

After the expense is added the program asks the user if he wants to continue adding expenses or wants to stop. If he wants to stop he is directed to the main menu again.

##### Showing the history of expenses:
In this part of the program we read all expenses from the expense list and render it for the user to see. After rendering the data the user is directed to the main menu again.

##### Exit the program:
When the user chooses to terminate the program, it tells the user it will exit the program and break the main loop of the program resulting in termination.

##### Misc:
For the data storage I opted for a json file as it is easy to implement and is independent of cloud services. It also gives room for improvement where in future versions of the programs it might be possible to add users of the program who all have their own expense file. This will make the program more complex and easier to use for multiple people.

I chose the dictionary data type for ease of use and because it seems to be the appropriate form for expense tracking. Furthermore it made it easier for saving in a JSON file.
