from project import viable_user_input, get_response_for_menu, get_expense, user_continue
from classes import Expense
from unittest.mock import patch

def main():
    test_true_viable_user_input()
    test_false_viable_user_input()
    test_get_expense()
    test_get_response_from_menu()
    test_true_user_continue()
    test_false_user_continue()

def test_true_viable_user_input():
    for _ in range(1, 4):
        assert viable_user_input(str(_)) == True    

def test_false_viable_user_input():
    for _ in range(4, 10):
        assert viable_user_input(str(_)) == False
    for _ in list('abcdefg'):
        assert viable_user_input(str(_)) == False

def test_get_expense():
    ...

def test_get_response_from_menu():
    with patch('builtins.input', return_value='1'):
        response = get_response_for_menu()
    assert response == '1'

def test_true_user_continue():
    ...

def test_false_user_continue():
    ...
    
if __name__ == "__main__":
    main()