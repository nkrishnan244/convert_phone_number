from create_dictionaries import get_dicts


class ConvertPhoneNumber:
    def __init__(self):
        self.letter2num, self.num2letter = get_dicts()

    def number_to_words(self, raw_phone_number):
        """
        Converts string representation of phone number to "wordified" phone number

        Parameters:
        raw_phone_number (String): string that represents phone number (with dashes)

        Returns:
        String: string representation of "wordified" phone number

        """

    def words_to_number(self, wordified_phone_number):
        """
        Converts string representation of "wordified" phone number to normal phone number

        Parameters:
        wordified_phone_number (String): string that represents "wordified" phone number

        Returns:
        String: string representation of phone number

        """

    def all_wordifications(self, raw_phone_number):
        """
        Converts string representation of phone number to all possible "wordified" phone numbers

        Parameters:
        raw_phone_number (String): string that represents phone number (with dashes)

        Returns:
        List: List of strings that are all possible "wordified" versions of input phone number

        """


ConvertPhoneNumber()