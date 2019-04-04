class StringCalculator:
    """ A simple string calculator that performs operations on numbers in a string. """

    def Add(self, text):
        """ Adds together all delimited numbers in a string"""
        if not isinstance(text, str):
            return 0

        total = 0

        if text.isdigit():
            total += int(text)

        return total