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
    If no delimiter is found, the default delimiter is a comma.
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
        """
        Adds together all unsigned delimited integers in a string and returns it.
        Delimiter is in the form: //[delimiter]\n
        Multiples of a delimiter can be used as a delimiter, eg. //***\n
        Multiple characters, separated by a comma, can be used as a delimiter.
        eg. //$,@\n
        Characters / and \n cannot be used as delimiters
        """
        if not isinstance(text, str):
            return 0

        total = 0
        delim = get_delimiter(text)
        sanitized_text = re.sub(DELIMITER_REGEX, '', text, 1)

        # checks if delimiter contains multiple delimiters or one of arbitrary length
        if delim == len(delim) * delim[0]:
            numeric_list = sanitized_text.split(delim)
        else:
            # converts delimiter to regex if there are multiples, and then splits
            # the string based on the regex
            delim_pattern = re.compile(re.escape(delim).replace(',', '|'))
            numeric_list = re.split(delim_pattern, sanitized_text)

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
