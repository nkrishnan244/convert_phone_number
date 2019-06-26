from create_dictionaries import get_dicts, get_word_list
from itertools import product
import pdb

class ConvertPhoneNumber:
    def __init__(self):
        self.letter2num, self.num2letter = get_dicts()
        self.word_list = get_word_list()
        self.total_words = []
        print(self.all_wordifications("1-804-232-7326"))
        print(self.words_to_number("1-800-fgh-6837"))

    def number_to_words(self, raw_phone_number):
        """
        Converts string representation of phone number to "wordified" phone number

        Parameters:
        raw_phone_number (String): string that represents phone number (with dashes)

        Returns:
        String: string representation of "wordified" phone number

        """
        num_elements = len(raw_phone_number)
        curr_string = ""
        string_to_list = []
        num_dashes = -1
        not_possible = False
        for i in range(num_elements - 1, -1, -1):  # Iterate backwards through phone number
            if not raw_phone_number[i] == '-':  # Only consider wordifying elements after a dash
                curr_string = raw_phone_number[i] + curr_string
            else:  # If we reach a dash
                num_dashes += 1  # Used for parsing output
                for element in curr_string:
                    if element not in self.num2letter:  # IF we have an element that can't be converted to a letter
                        not_possible = True
                        break
                    string_to_list.append(self.num2letter[element])  # Convert each number into a list of letters
                if not_possible:
                    return "Wordification Failed"
                all_combinations = list(product(*string_to_list))  # Find all possible combinations of letters
                for char_list in all_combinations:
                    curr_word = ''.join(char_list)  # Convert combination of letters into string
                    if curr_word in self.word_list:  # Check if the word exists
                        length = len(curr_word)
                        # Create and store wordified number
                        wordified_num = raw_phone_number[0:num_elements - length - num_dashes] + curr_word.upper()
                        return wordified_num


    def words_to_number(self, wordified_phone_number):
        """
        Converts string representation of "wordified" phone number to normal phone number

        Parameters:
        wordified_phone_number (String): string that represents "wordified" phone number

        Returns:
        String: string representation of phone number

        """
        phone_number = ""
        for i in range(0, len(wordified_phone_number)):
            if wordified_phone_number[i].isalpha():  # IF element is a letter
                phone_number += self.letter2num[wordified_phone_number[i]]  # Convert to number
            else:
                phone_number += wordified_phone_number[i]
        return phone_number

    def find_substr(self, num, curr_string):
        for i in range(len(num) - 1, -1, -1):
            words = self.find_all_words(num[i:len(num)])
            if words:
                for word in words:
                    self.total_words.append(word + curr_string)
                    self.find_substr(num[0:i], word + curr_string)

    def all_wordifications(self, raw_phone_number):
        """
        Converts string representation of phone number to all possible "wordified" phone numbers

        Parameters:
        raw_phone_number (String): string that represents phone number (with dashes)

        Returns:
        List: List of strings that are all possible "wordified" versions of input phone number

        """
        dashless_phone_number = raw_phone_number.replace('-', '')

        for i in range(len(dashless_phone_number) - 1, -1, -1):
            if dashless_phone_number[i] not in self.num2letter:
                left_most_element = i + 1
                break

        reduced_phone_num = dashless_phone_number[left_most_element:]
        self.find_substr(reduced_phone_num, "")


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