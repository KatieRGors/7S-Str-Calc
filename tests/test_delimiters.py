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


def test_delimiter_none_given():
    input_text = "1,2,3"
    expected_delimiter = ','
    assert expected_delimiter == get_delimiter(input_text)


def test_delimiter_semicolon_string():
    input_text = "//;\n1;3;4"
    expected_delimiter = ';'
    assert expected_delimiter == get_delimiter(input_text)


def test_delimiter_dollar_string():
    input_text = "//$\n1$2$3"
    expected_delimiter = '$'
    assert expected_delimiter == get_delimiter(input_text)


def test_delimiter_at_string():
    input_text = "//@\n2@3@8"
    expected_delimiter = '@'
    assert expected_delimiter == get_delimiter(input_text)


def test_delimiter_at_string_malformed_extra_slash():
    input_text = "///@\n"
    expected_delimiter = ','
    assert expected_delimiter == get_delimiter(input_text)


def test_delimiter_at_string_malformed_extra_newline():
    input_text = "//\n@\n"
    expected_delimiter = ','
    assert expected_delimiter == get_delimiter(input_text)


def test_delimiter_at_string_malformed_numeric():
    input_text = "//0@\n"
    expected_delimiter = ','
    assert expected_delimiter == get_delimiter(input_text)


# BONUS 2

def test_delimiter_star_multiples():
    input_text = "//***\n"
    expected_delimiter = '***'
    assert expected_delimiter == get_delimiter(input_text)


def test_delimiter_comma_multiples():
    input_text = "//,,,,\n"
    expected_delimiter = ',,,,'
    assert expected_delimiter == get_delimiter(input_text)


# BONUS 3

def test_multiple_delimiters():
    input_text = "//$,@\n"
    expected_delimiter = '$,@'
    assert expected_delimiter == get_delimiter(input_text)


def test_multiple_delimiters_with_multiples():
    input_text = "//$,@@@\n"
    expected_delimiter = '$,@@@'
    assert expected_delimiter == get_delimiter(input_text)
