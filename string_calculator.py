import re

MAX_ADDITION_PARAM = 1000
MIN_ADDITION_PARAM = 0

DEFAULT_DELIMITER = ','
DELIMITER_DEFINITION_BEGINNING = '//'
DELIMITER_DEFINITION_ENDING = '\n'
DELIMITER_REGEX = r'^//[^\d\n/]+\n'


def get_delimiter(text):
    """
    Returns the delimiter parsed from given text. Delimiter is in the form
    //[delimiter]\n
    If no delimiter is found, the default delimiter is a comma
    / and \n cannot be used as delimiters
    """
    if isinstance(text, str):
        result = re.search(DELIMITER_REGEX, text)
        if result is not None:
            sanitized_result = result.group()
            sanitized_result = sanitized_result.replace(DELIMITER_DEFINITION_BEGINNING, '')
            sanitized_result = sanitized_result.replace(DELIMITER_DEFINITION_ENDING, '')
            return sanitized_result

    return DEFAULT_DELIMITER


class StringCalculator:
    """ A simple string calculator that performs operations on numbers in a string. """

    def Add(self, text):
        """ Adds together all delimited numbers in a string"""
        if not isinstance(text, str):
            return 0

        total = 0
        delim = get_delimiter(text)
        numeric_list = re.sub(DELIMITER_REGEX, '', text, 1).split(delim)

        for element in numeric_list:
            sanitized_element = element.replace('\n', '')

            try:
                number = int(sanitized_element)

                if number < MIN_ADDITION_PARAM:
                    raise Exception("Negatives not allowed. You entered: " + sanitized_element)
                elif number <= MAX_ADDITION_PARAM:
                    total += int(sanitized_element)
            except ValueError:
                print("Number was invalid")

        return total
