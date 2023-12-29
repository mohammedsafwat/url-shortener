import pytest
from url_shortener import URLShortener
from short_code_generator import ShortCodeGenerator
from unittest.mock import Mock


@pytest.fixture
def short_code_generator_mock():
    short_code_generator = Mock()
    short_code_generator.generate_short_code.return_value = "AaBb12"
    return short_code_generator


def test_short_code_generation(short_code_generator_mock):
    # Given
    long_url = "https://www.test.com"
    url_shortener = URLShortener(short_code_generator_mock)

    # When
    short_url_code = url_shortener.shorten_url(long_url)

    # Then
    assert short_url_code == "AaBb12"