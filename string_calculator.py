class StringCalculator:
    """ A simple string calculator that performs operations on numbers in a string. """

    def Add(self, text):
        """ Adds together all delimited numbers in a string"""
        if not isinstance(text, str):
            return 0

        total = 0
        sanitized_text = text.replace('\n', '')
        numeric_list = sanitized_text.split(',')

        # todo support negatives? floats?
        for element in numeric_list:
            if element.isdigit() and int(element) <= 1000:
                total += int(element)

        return total
