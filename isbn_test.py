import pytest

from isbn import is_valid

def test_valid_isbn_number():
    assert is_valid('3-598-21508-8')

def test_invalid_check_digit():
    assert not is_valid('3-598-21508-9')

def test_valid_with_X_check_digit():
    assert is_valid('3-598-21507-X')

def test_invalid_check_digit_other_than_X():
    assert not is_valid('3-598-21507-A')

def test_invalid_character_in_isbn():
    assert not is_valid('3-598-P1581-X')

def test_invalid_X_other_than_check_digit():
    assert not is_valid('3-598-2X507-9')

def test_valid_isbn_without_separating_dashes():
    assert is_valid('3598215088')

def test_valid_isbn_without_separating_dashes_with_X_check_digit():
    assert is_valid('359821507X')

def test_invalid_isbn_without_check_digit_and_dashes():
    assert not is_valid('359821507')

def test_invalid_too_long_isbn_with_no_dashes():
    assert not is_valid('3598215078X')

def test_invalid_too_short_isbn():
    assert not is_valid('00')

def test_invalid_isbn_without_check_digit():
    assert not is_valid('3-598-21507')

def test_invalid_check_digit_X_used_for_0():
    assert not is_valid('3-598-21515-X')

def test_valid_empty_isbn():
    assert not is_valid('')

def test_input_is_nine_characters():
    assert not is_valid('134456729')

def test_invalid_characters_are_not_ignored():
    assert not is_valid('3132P34035')

def test_input_is_too_long_but_contains_a_valid_isbn():
    assert not is_valid('98245726788')
