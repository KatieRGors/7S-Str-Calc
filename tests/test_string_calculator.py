import pytest

from string_calculator import StringCalculator


def check_calculator(input_text, expected_output):
    actual_output = StringCalculator().Add(input_text)
    assert expected_output == actual_output


# PART 1

def test_empty_string():
    input_text = ""
    expected_output = 0
    check_calculator(input_text, expected_output)


def test_none_instead_of_string():
    input_text = None
    expected_output = 0
    check_calculator(input_text, expected_output)


def test_integer_instead_of_string():
    input_text = 1
    expected_output = 0
    check_calculator(input_text, expected_output)


def test_one_element_all_valid():
    input_text = "1"
    expected_output = 1
    check_calculator(input_text, expected_output)


def test_one_element_none_valid():
    input_text = "a"
    expected_output = 0
    check_calculator(input_text, expected_output)


def test_two_elements_all_valid():
    input_text = "1,1"
    expected_output = 2
    check_calculator(input_text, expected_output)


def test_three_elements_all_valid():
    input_text = "1,2,5"
    expected_output = 8
    check_calculator(input_text, expected_output)


def test_three_elements_some_invalid():
    input_text = "\n,a,5"
    expected_output = 5
    check_calculator(input_text, expected_output)


# PART 2

def test_three_elements_with_post_newlines_all_valid():
    input_text = "1\n,2,3"
    expected_output = 6
    check_calculator(input_text, expected_output)


def test_three_elements_with_pre_newlines_all_valid():
    input_text = "1,\n2,4"
    expected_output = 7
    check_calculator(input_text, expected_output)


def test_two_elements_one_larger_than_1000():
    input_text = "2,1001"
    expected_output = 2
    check_calculator(input_text, expected_output)


def test_two_elements_one_equal_to_1000():
    input_text = "2,1000"
    expected_output = 1002
    check_calculator(input_text, expected_output)


# PART 3

def test_three_elements_with_custom_delimiter_semicolon():
    input_text = "//;\n1;3;4"
    expected_output = 8
    check_calculator(input_text, expected_output)


def test_three_elements_with_custom_delimiter_dollar():
    input_text = "//$\n1$2$3"
    expected_output = 6
    check_calculator(input_text, expected_output)


def test_three_elements_with_custom_delimiter_at():
    input_text = "//@\n2@3@8"
    expected_output = 13
    check_calculator(input_text, expected_output)


# PART 4

def test_one_element_with_negative():
    input_text = "-1"
    with pytest.raises(Exception):
        StringCalculator().Add(input_text)


def test_three_elements_with_negative():
    input_text = "1,-1,100"
    with pytest.raises(Exception):
        StringCalculator().Add(input_text)


def test_three_elements_with_float():
    input_text = "1,1.5,100"
    expected_output = 101
    check_calculator(input_text, expected_output)


# BONUS 2
def test_multiple_elements_with_longer_delimiter():
    input_text = "//***\n1***2***3"
    expected_output = 6
    check_calculator(input_text, expected_output)

