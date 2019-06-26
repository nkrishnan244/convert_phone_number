from create_dictionaries import get_dicts, get_word_list, include_dashes
from itertools import product
import pdb
import random

class ConvertPhoneNumber:
    def __init__(self):
        self.letter2num, self.num2letter = get_dicts()
        self.word_list = get_word_list()
        self.total_words = []
        print(self.number_to_words("3333"))

    def number_to_words(self, raw_phone_number):
        """
        Converts string representation of phone number to "wordified" phone number

        Parameters:
        raw_phone_number (String): string that represents phone number (with dashes)

        Returns:
        String: string representation of "wordified" phone number

        """
        dashless_phone_number = raw_phone_number.replace('-', '')  # Get rid of all dashes

        for i in range(len(dashless_phone_number) - 1, -1, -1):
            index_from_back = len(dashless_phone_number) - i
            # Only possible to wordify last 4 elements, or every last 3 elements after that (4, 7, 10, etc)
            possible_wordify = index_from_back == 4 or (index_from_back > 4 and (index_from_back - 4) % 3 == 0)
            if possible_wordify:
                words = self.find_all_words(dashless_phone_number[i:len(dashless_phone_number)])
                if len(words) != 0: # As soon as it is possible to wordify, Do it!
                    word_index = random.randint(0, len(words)-1) # Randomly select a word
                    dashless_phone_number = dashless_phone_number[0:i] + words[word_index].upper()  # Wordify!
                    return include_dashes(dashless_phone_number)  # Add dashes to phone number
        return "Unable to wordify"  # Very sad!

    def words_to_number(self, wordified_phone_number):
        """
        Converts string representation of "wordified" phone number to normal phone number

        Parameters:
        wordified_phone_number (String): string that represents "wordified" phone number

        Returns:
        String: string representation of phone number

        """
        dashless_phone_number = wordified_phone_number.replace('-', '')  # Get rid of dashes
        dashless_phone_number = dashless_phone_number.lower()  # Everything must be lower case to search in dictionary

        phone_number = ""

        for i in range(len(dashless_phone_number)-1, -1, -1):
            if dashless_phone_number[i].isalpha():  # IF element is a letter, add to phone number
                phone_number = self.letter2num[dashless_phone_number[i]] + phone_number
            else:
                phone_number = dashless_phone_number[i] + phone_number

            if not i == 0: # Prevents dash from being added at front of number
                index_from_back = len(dashless_phone_number) - i
                # Only add dash after last 4 elements, or every last 3 elements after that (4, 7, 10, etc)
                if index_from_back == 4 or (index_from_back > 4 and (index_from_back - 4) % 3 == 0):
                    phone_number = "-" + phone_number
        print(phone_number)

        return phone_number

    def find_substr(self, num, curr_string, raw_phone_number):
        """
        Finds all possible substrings from a string of numbers and adds it to self.total_words

        Parameters:
        num (String): string that represents a series of numbers
        curr_string (String): string that represents ...
        raw_phone_number (String): original phone number

        """
        for i in range(len(num) - 1, -1, -1):
            words = self.find_all_words(num[i:len(num)])
            if words:  # if the substring of digits can be converted to at least one word
                for word in words:
                    new_words = word + curr_string  # combine current word and new word
                    if len(new_words) == 4 or (len(new_words) - 4) % 3 == 0: # Only wordify if we are at 4, 7, 10, etc
                        num_dashes = 0
                        if len(new_words) != 4:
                            num_dashes = int((len(new_words) - 4)/3) # Number of dashes for concatenation
                            final_element = len(raw_phone_number) - len(new_words) - num_dashes
                        self.total_words.append(raw_phone_number[0:final_element] + new_words.upper())  # Save string
                    self.find_substr(num[0:i], new_words, raw_phone_number)  # Find substrings before current words

    def all_wordifications(self, raw_phone_number):
        """
        Converts string representation of phone number to all possible "wordified" phone numbers

        Parameters:
        raw_phone_number (String): string that represents phone number (with dashes)

        Returns:
        List: List of strings that are all possible "wordified" versions of input phone number

        """
        dashless_phone_number = raw_phone_number.replace('-', '')  # Get rid of dashes
        left_most_element = 0

        # Can't wordify anything past a 0 or a 1
        for i in range(len(dashless_phone_number) - 1, -1, -1):
            if dashless_phone_number[i] not in self.num2letter:
                left_most_element = i + 1
                break

        reduced_phone_num = dashless_phone_number[left_most_element:]

        # Find all possible sub-words of the entire phone number
        self.total_words = []
        self.find_substr(reduced_phone_num, "", raw_phone_number)
        return self.total_words


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
                length = len(curr_word)
                # Create and store wordified number
                words.append(curr_word)
        return words



ConvertPhoneNumber()