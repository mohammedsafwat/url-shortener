# A class used for URL storage operations.
class URLStorage:

    __url_storage = {}

    def store_short_url(self, short_url_code, long_url):
        self.__url_storage[short_url_code] = long_url

    def get_long_url(self, short_url_code):
        if short_url_code in self.__url_storage:
            return self.__url_storage[short_url_code]
        return None

    def get_short_url_code(self, long_url):
        for key, value in self.__url_storage.items():
            if value == long_url:
                return key
        return None
