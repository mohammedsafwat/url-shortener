import pytest
from url_storage import URLStorage


@pytest.fixture
def url_storage():
    return URLStorage()


@pytest.mark.parametrize("short_url_code,long_url,random_short_url_code", [
    ("test_short_url_code", "test_long_url", "random_short_url_code"),
])
def test_short_url_to_long_url_mapping(url_storage, short_url_code, long_url, random_short_url_code):
    # When
    url_storage.store_short_url(short_url_code, long_url)

    # Then
    assert url_storage.get_long_url(short_url_code) is not None
    assert url_storage.get_long_url(short_url_code) == long_url
    assert url_storage.get_long_url(random_short_url_code) is None


@pytest.mark.parametrize("short_url_code,long_url,random_long_url", [
    ("test_short_url_code", "test_long_url", "random_long_url"),
])
def test_long_url_to_short_url_mapping(url_storage, short_url_code, long_url, random_long_url):
    # When
    url_storage.store_short_url(short_url_code, long_url)

    # Then
    assert url_storage.get_short_url_code(long_url) is not None 
    assert url_storage.get_short_url_code(long_url) == short_url_code
    assert url_storage.get_long_url(random_long_url) is None