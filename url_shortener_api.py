from constants import Constants
from errors import Errors
from flask import Flask, jsonify, request
from short_code_generator import ShortCodeGenerator
from url_formatter import URLFormatter
from urllib.parse import urlparse
from url_storage import URLStorage
from url_shortener import URLShortener


# App initialization.
app = Flask(__name__)

__short_code_generator = ShortCodeGenerator(Constants.SHORT_URL_CODE_LENGTH)
__url_shortener = URLShortener(__short_code_generator)
__url_storage = URLStorage()
__url_formatter = URLFormatter()


# Decode a short URL code to its original form.
@app.route('/decode/<string:short_url_code>', methods=['GET'])
def decode(short_url_code):
    if __url_storage.get_long_url(short_url_code) != None:
        return jsonify(
            {
                Constants.JSONKeys.DECODED_URL: __url_storage.get_long_url(
                    short_url_code)
            }
        )
    return jsonify(
        {
            Constants.JSONKeys.ERROR: Errors.URL_DECODE_ERROR
        }
    )


# Encode a long URL to a short URL.
@app.route('/encode', methods=['POST'])
def encode():
    url_root = request.url_root
    long_url = request.get_json().get(Constants.JSONKeys.URL)

    # Check if the input value is a valid URL.
    if not (urlparse(long_url).scheme and urlparse(long_url).netloc):
        return jsonify(
            {
                Constants.JSONKeys.ERROR: Errors.INVALID_URL_ERROR
            }
        )

    short_url_code = __url_storage.get_short_url_code(long_url)

    # If no mapping exists for the long url, create a new
    # short url code and store it.
    if short_url_code == None:
        short_url_code = __url_shortener.shorten_url(long_url)
        __url_storage.store_short_url(short_url_code, long_url)

    return jsonify(
        {
            Constants.JSONKeys.ENCODED_URL: __url_formatter.format_short_url(
                url_root, short_url_code)
        }
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
