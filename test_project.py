from project import viable_user_input, validate_amount, validate_category, validate_date, user_continue
from classes import Expense
from unittest.mock import patch

def main():
    test_viable_user_input()
    test_validate_amount()
    test_validate_category()
    test_validate_date()
    test_user_continue()

def test_viable_user_input():
    for _ in range(1, 4):
        assert viable_user_input(str(_)) == True    
    for _ in range(4, 10):
        assert viable_user_input(str(_)) == False
    for _ in list('abcdefg'):
        assert viable_user_input(str(_)) == False

def test_validate_amount():
    test_values = [i for i in range(1, 100)]

    for _ in test_values:
        with patch('builtins.input', return_value=f"{_}"):
            float = validate_amount()
        assert float == f"{_}" + ".00"

    with patch('builtins.input', return_value='12.22'):
        float = validate_amount()
    assert float == '12.22'

def test_validate_category():
    test_values = 'abcdefghijk'
    for _ in test_values:
        with patch('builtins.input', return_value=f"{_}"):
            category = validate_category()
        assert category == _.title()

def test_validate_date():
    with patch('builtins.input', return_value='2024/12/20'):
        valid = validate_date()
    assert valid == '2024/12/20'

def test_user_continue():
    assert user_continue('') == True
    
    fail_list = 'asdfghj'
    for _ in fail_list:
        assert user_continue(f"{_}") == False
    
if __name__ == "__main__":
    main()