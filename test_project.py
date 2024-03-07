from project import viable_user_input, get_expense, get_response_for_menu
from classes import Expense
from unittest.mock import patch

def main():
    test_true_viable_user_input()
    test_false_viable_user_input()
    test_get_expense()
    test_get_response_from_menu()

def test_true_viable_user_input():
    assert viable_user_input('1') == True
    assert viable_user_input('2') == True
    assert viable_user_input('3') == True    

def test_false_viable_user_input():
    for _ in range(4, 10):
        assert viable_user_input(str(_)) == False

def test_get_expense():
    ...

def test_get_response_from_menu():
    with patch('builtins.input', return_value='1'):
        response = get_response_for_menu()
    assert response == '1'


if __name__ == "__main__":
    main()