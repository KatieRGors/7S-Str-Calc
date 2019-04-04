from string_calculator import StringCalculator

def test_empty_string():
    input_text = ""
    expected_output = 0
    actual_output = StringCalculator().Add(input_text)
    assert expected_output == actual_output


def test_none_instead_of_string():
    input_text = None
    expected_output = 0
    actual_output = StringCalculator().Add(input_text)
    assert expected_output == actual_output


def test_integer_instead_of_string():
    input_text = 1
    expected_output = 0
    actual_output = StringCalculator().Add(input_text)
    assert expected_output == actual_output

