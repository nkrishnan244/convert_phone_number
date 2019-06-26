from convert_phone_num import ConvertPhoneNumber
import unittest

class TestConvertPhoneNumber(unittest.TestCase):
    def setUp(self):
        self.convert_phone_num_ = ConvertPhoneNumber()

    # Unit test doesn't make sense
    def test_number_to_words(self):
        test_cases = [
            "18007246837", # Given example (PASS)
            "1-800-724-6837", # Given example with dashes (PASS)
            "800-724-6837", # Given example without leading 1 (PASS)
            "800-724-7777", # Impossible to make a word (PASS)
            "180072468370" # Impossible (PASS)
        ]
        print("///////////////////////////////  TESTING NUMBER TO WORDS ///////////////////////////////")
        for test_string in test_cases:
            print(self.convert_phone_num_.number_to_words(test_string))

        print("///////////////////////////////  DONE TESTING NUMBER TO WORDS ///////////////////////////////")

    # Unit test
    def test_words_to_number(self):
        self.assertEqual(self.convert_phone_num_.words_to_number("1-800-PAINTER"), "1-800-724-6837")
        self.assertEqual(self.convert_phone_num_.words_to_number("1800PAINTER"), "1-800-724-6837")
        self.assertEqual(self.convert_phone_num_.words_to_number("1800painter"), "1-800-724-6837")
        self.assertEqual(self.convert_phone_num_.words_to_number("1-800-724-6837"), "1-800-724-6837")
        self.assertEqual(self.convert_phone_num_.words_to_number("800724paint"), "8-007-247-2468")
        self.assertEqual(self.convert_phone_num_.words_to_number("a-bcd-efg-hijk"), "2-223-334-4455")
        self.assertEqual(self.convert_phone_num_.words_to_number("A-BCD-EFG-HIJK"), "2-223-334-4455")
        self.assertEqual(self.convert_phone_num_.words_to_number("l-mno-pqr-stuv"), "5-666-777-7888")
        self.assertEqual(self.convert_phone_num_.words_to_number("L-MNO-PQR-STUV"), "5-666-777-7888")
        self.assertEqual(self.convert_phone_num_.words_to_number("wxyz"), "9999")
        self.assertEqual(self.convert_phone_num_.words_to_number("WXYZ"), "9999")

    # Unit test doesn't make sense
    def test_all_wordifications(self):
        test_cases = [
            "18007246837", # Given example (PASS)
            "1-800-724-6837", # Given example with dashes (PASS)
            "800-724-6837", # Given example without leading 1 (PASS)
            "800-724-7777", # Impossible to make a word (PASS)
            "180072468370", # Impossible (PASS)
            "362-399-5464", # EMBEZZLING (PASS)
        ]
        print("/////////////////////////////// TESTING ALL WORDIFICATIONS ///////////////////////////////")
        for test_string in test_cases:
            print(self.convert_phone_num_.all_wordifications(test_string))
        print("/////////////////////////////// DONE TESTING ALL WORDIFICATIONS ///////////////////////////////")

if __name__ == '__main__':
    unittest.main()
