from create_dictionaries import get_dicts, get_word_list
from itertools import product
import pdb

class ConvertPhoneNumber:
    def __init__(self):
        self.letter2num, self.num2letter = get_dicts()
        self.word_list = get_word_list()
        self.total_words = []
        print(self.all_wordifications(self.words_to_number("215-283-LEAD")))
        print(self.number_to_words("215-283-5323"))

    def number_to_words(self, raw_phone_number):
        """
        Converts string representation of phone number to "wordified" phone number

        Parameters:
        raw_phone_number (String): string that represents phone number (with dashes)

        Returns:
        String: string representation of "wordified" phone number

        """
        dashless_phone_number = raw_phone_number.replace('-', '')

        for i in range(len(dashless_phone_number) - 1, -1, -1):
            possible_wordify = (len(dashless_phone_number) - i) == 4 or (len(dashless_phone_number) - i) > 4 and (len(dashless_phone_number) - i - 4)%3 == 0
            if possible_wordify:
                words = self.find_all_words(dashless_phone_number[i:len(dashless_phone_number)])
                if len(words) != 0:
                    dashless_phone_number = dashless_phone_number[0:i] + words[0].upper()
                    return self.include_dashes(dashless_phone_number)
        return "Unable to wordify"

    def include_dashes(self, dashless_phone_number):
        phone_number = ""
        for i in range(len(dashless_phone_number) - 1, -1, -1):
            phone_number = dashless_phone_number[i] + phone_number
            if not i == 0:
                if (len(dashless_phone_number) - i) == 4 or (len(dashless_phone_number) - i) > 4 and (len(dashless_phone_number) - i - 4)%3 == 0:
                    phone_number = "-" + phone_number
        return phone_number


    def words_to_number(self, wordified_phone_number):
        """
        Converts string representation of "wordified" phone number to normal phone number

        Parameters:
        wordified_phone_number (String): string that represents "wordified" phone number

        Returns:
        String: string representation of phone number

        """
        dashless_phone_number = wordified_phone_number.replace('-', '')
        dashless_phone_number = dashless_phone_number.lower()

        phone_number = ""

        for i in range(len(dashless_phone_number)-1, -1, -1):
            if dashless_phone_number[i].isalpha():  # IF element is a letter
                phone_number = self.letter2num[dashless_phone_number[i]] + phone_number
            else:
                phone_number = dashless_phone_number[i] + phone_number
            print(i)
            if not i == 0:
                if (len(dashless_phone_number) - i) == 4 or (len(dashless_phone_number) - i) > 4 and (len(dashless_phone_number) - i - 4)%3 == 0:
                    phone_number = "-" + phone_number
        print(phone_number)

        return phone_number

    def find_substr(self, num, curr_string, raw_phone_number):
        num_elements = len(raw_phone_number)
        for i in range(len(num) - 1, -1, -1):
            words = self.find_all_words(num[i:len(num)])
            if words:
                for word in words:
                    new_words = word + curr_string
                    if len(new_words) == 4 or (len(new_words) - 4) % 3 == 0:
                        num_dashes = 0
                        if len(new_words) != 4:
                            num_dashes = int((len(new_words) - 4)/3)
                        self.total_words.append(raw_phone_number[0:(len(raw_phone_number) - len(new_words) - num_dashes)] + new_words.upper())
                    self.find_substr(num[0:i], new_words, raw_phone_number)

    def all_wordifications(self, raw_phone_number):
        """
        Converts string representation of phone number to all possible "wordified" phone numbers

        Parameters:
        raw_phone_number (String): string that represents phone number (with dashes)

        Returns:
        List: List of strings that are all possible "wordified" versions of input phone number

        """
        dashless_phone_number = raw_phone_number.replace('-', '')
        left_most_element = 0

        for i in range(len(dashless_phone_number) - 1, -1, -1):
            if dashless_phone_number[i] not in self.num2letter:
                left_most_element = i + 1
                break

        reduced_phone_num = dashless_phone_number[left_most_element:]
        self.find_substr(reduced_phone_num, "", raw_phone_number)
        print(self.total_words)


    def find_all_words(self, numbers):
        """
        Converts string representation of number to all possible words

        Parameters:
        numbers (String): string that represents number

        Returns:
        List: List of strings that are all possible "wordified" versions of number

        """
        string_to_list = []
        words = []
        for element in numbers:
            if element not in self.num2letter:  # IF we have an element that can't be converted to a letter
                return words
            string_to_list.append(self.num2letter[element])  # Convert each number into a list of letters
        all_combinations = list(product(*string_to_list))  # Find all possible combinations of letters
        for char_list in all_combinations:
            curr_word = ''.join(char_list)  # Convert combination of letters into string
            # For some reason every dictionary includes the letters of the alphabet
            if curr_word in self.word_list and len(curr_word) > 2:  # Check if the word exists (size for readability)
            # if curr_word in self.word_list and (curr_word == 'a' or len(curr_word) > 1):  # Check if the word exists
                length = len(curr_word)
                # Create and store wordified number
                words.append(curr_word)
        return words



ConvertPhoneNumber()