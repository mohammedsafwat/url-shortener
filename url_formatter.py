# A class used for URL formatting operations.
class URLFormatter:

    def format_short_url(self, url_root, short_url_code):
        return '{url_root}{short_url_code}'.format(url_root=url_root, short_url_code=short_url_code)
