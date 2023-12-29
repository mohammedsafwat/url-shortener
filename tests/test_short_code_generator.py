import pytest
from short_code_generator import ShortCodeGenerator

short_code_length = 8
long_url = "https://www.test.com/"

@pytest.fixture
def short_code_generator():
    short_code_generator = ShortCodeGenerator(short_code_length)
    return short_code_generator


def test_short_code_length(short_code_generator):
    # When
    generated_short_code = short_code_generator.generate_short_code(long_url)

    # Then
    assert len(generated_short_code) == short_code_length


def test_short_code_is_capitalized(short_code_generator):
    # When
    generated_short_code = short_code_generator.generate_short_code(long_url)
    print(generated_short_code)

    # Then
    assert generated_short_code[0].isupper()