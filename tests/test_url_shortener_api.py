import pytest
from url_shortener_api import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_encode_endpoint_response_content_type_is_json(client):
    # Given
    encode_endpoint = '/encode'

    # When
    response = client.post(encode_endpoint, json={})

    # Then
    assert response.content_type == "application/json"


def test_encode_valid_url_returns_success_response(client):
    # Given
    encode_endpoint = '/encode'
    post_request_body = {"url": "https://codesubmit.io/library/react"}

    # When
    response = client.post(encode_endpoint, json=post_request_body)

    # Then
    assert response.get_json().get("encoded_url") is not None
    assert response.get_json().get("error") is None
    assert response.request.url_root in response.get_json().get("encoded_url")


def test_encode_invalid_url_returns_error(client):
    # Given
    encode_endpoint = '/encode'
    post_request_body = {"url": "codesubmit"}

    # When
    response = client.post(encode_endpoint, json=post_request_body)

    # Then
    assert response.get_json().get("encoded_url") is None
    assert response.get_json().get("error") is not None
    assert response.get_json().get("error") == "The input argument is not a valid URL."


def test_decode_endpoint_response_content_type_is_json(client):
    # Given
    decode_endpoint = '/decode/AaBb12'

    # When
    response = client.get(decode_endpoint)

    # Then
    assert response.content_type == "application/json"


def test_decode_exisiting_url_returns_success_response(client):
    # Given
    long_url = "https://codesubmit.io/library/react"
    encode_endpoint = '/encode'
    decode_endpoint = '/decode/{short_url_code}'
    post_request_body = {"url": long_url}

    # When
    encode_response = client.post(encode_endpoint, json=post_request_body)
    encoded_url = encode_response.get_json().get("encoded_url")
    encoded_url_short_code = encoded_url.split('/')[-1]
    decode_response = client.get(decode_endpoint.format(short_url_code=encoded_url_short_code))

    # Then
    assert decode_response.get_json().get("decoded_url") == long_url


def test_decode_non_existing_url_returns_error(client):
    # Given
    decode_endpoint = '/decode/AaBb12'

    # When
    response = client.get(decode_endpoint)

    # Then
    assert response.get_json().get("error") is not None
    assert response.get_json().get("error") == "No URL found for the input short URL code."


def test_encode_same_url_returns_same_short_code(client):
    # Given
    encode_endpoint = '/encode'
    first_post_request_body = {"url": "https://codesubmit.io/library/react"}
    second_post_request_body = {"url": "https://codesubmit.io/library/vue"}

    # When
    first_response = client.post(encode_endpoint, json=first_post_request_body)
    second_response = client.post(encode_endpoint, json=first_post_request_body)
    third_response = client.post(encode_endpoint, json=second_post_request_body)

    # Then
    assert first_response.get_json().get("encoded_url") == second_response.get_json().get("encoded_url")
    assert first_response.get_json().get("encoded_url") != third_response.get_json().get("encoded_url")
    assert second_response.get_json().get("encoded_url") != third_response.get_json().get("encoded_url")

