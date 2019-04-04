from string_calculator import get_delimiter

# PART 3
def test_delimiter_no_string():
    input_text = None
    expected_delimiter = ','
    assert expected_delimiter == get_delimiter(input_text)


def test_delimiter_empty_string():
    input_text = ""
    expected_delimiter = ','
    assert expected_delimiter == get_delimiter(input_text)


def test_delimiter_comma_string():
    input_text = ","
    expected_delimiter = ','
    assert expected_delimiter == get_delimiter(input_text)
