import pytest
from url_formatter import URLFormatter


def test_format_short_url():
    # Given
    url_formatter = URLFormatter()
    url_root = "https://www.example.com/"
    short_url_code = "Aa12Bb"

    # When
    formatted_url = url_formatter.format_short_url(url_root, short_url_code)

    # Then
    assert formatted_url == "{}{}".format(url_root, short_url_code)