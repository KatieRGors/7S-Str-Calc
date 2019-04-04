from string_calculator import StringCalculator

def test_empty_string():
    input_text = ""
    expected_output = 0
    actual_output = StringCalculator().Add(input_text)
    assert expected_output == actual_output
