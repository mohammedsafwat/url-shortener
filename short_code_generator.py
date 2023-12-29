import hashlib
import random
import string


# A class used for short code generation operations.
class ShortCodeGenerator:

    __short_code_length = None

    def __init__(self, short_code_length):
        self.__short_code_length = short_code_length

    def generate_short_code(self, input):
        first_letter = ''.join(random.choice(string.ascii_letters) for _ in range(1))
        hex_encoded_value = hashlib.md5(input.encode()).hexdigest()
        short_code = "{}{}".format(first_letter, hex_encoded_value).capitalize()[
            :self.__short_code_length]
        return short_code
