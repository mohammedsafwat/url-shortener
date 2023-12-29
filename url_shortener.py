# A class used for URL shortening operations.
class URLShortener:

    __short_code_generator = None

    def __init__(self, short_code_generator):
        self.__short_code_generator = short_code_generator

    def shorten_url(self, long_url):
        short_code = self.__short_code_generator.generate_short_code(long_url)
        return short_code
