# https://stackoverflow.com/questions/874017/python-load-words-from-file-into-a-set
def include_dashes(dashless_phone_number):
    """
    Adds proper dashes to phone numbers

    Parameters:
    dashless_phone_number (String): string that represents phone number (without dashes)

    Returns:
    String: string representation of phone number (with dashes)

    """
    phone_number = ""
    for i in range(len(dashless_phone_number) - 1, -1, -1):
        phone_number = dashless_phone_number[i] + phone_number
        if not i == 0:  # Prevents dash from being added at front of number
            index_from_back = len(dashless_phone_number) - i
            # Only add dash after last 4 elements, or every last 3 elements after that (4, 7, 10, etc)
            if index_from_back == 4 or (index_from_back > 4 and (index_from_back - 4) % 3 == 0):
                phone_number = "-" + phone_number
    return phone_number

def get_word_list():
    word_list = set(line.strip() for line in open('american-english.txt'))
    return word_list

def get_dicts():
    letter2num = {
        "a": "2",
        "b": "2",
        "c": "2",
        "d": "3",
        "e": "3",
        "f": "3",
        "g": "4",
        "h": "4",
        "i": "4",
        "j": "5",
        "k": "5",
        "l": "5",
        "m": "6",
        "n": "6",
        "o": "6",
        "p": "7",
        "q": "7",
        "r": "7",
        "s": "7",
        "t": "8",
        "u": "8",
        "v": "8",
        "w": "9",
        "x": "9",
        "y": "9",
        "z": "9"
    }

    num2letter = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    return letter2num, num2letter

