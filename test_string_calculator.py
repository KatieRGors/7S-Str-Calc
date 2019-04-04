from string_calculator import StringCalculator


def check_calculator(input_text, expected_output):
    actual_output = StringCalculator().Add(input_text)
    assert expected_output == actual_output


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


def test_three_elements_some_ivalid():
    input_text = "\n,a,5"
    expected_output = 5
    check_calculator(input_text, expected_output)
