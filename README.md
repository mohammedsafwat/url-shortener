### Description
A Flask application exposing two endpoints for encoding and decoding URLs.

### Environemt preparation
- It's recommended to use Python3. Make sure it's installed on your machine. You can follow the steps mentioned [here](https://docs.python-guide.org/starting/install3/osx/).
- Install `virtualenv` using `pip3 install virtualenv`.
- Create a new Python virtual environment using `python3 -m venv env`. The virtual environment in this case is called `env`.
- Activate the virtual environment using `source env/bin/activate`.
- Install all modules defined in `requirements.text` using `python3 -m pip install -r requirements.txt`.

### How to run the app
- To start the Flask app, run `python3 url_shortener_api.py` in the root directory. A new dev server will start and will run. You should see something like the following in your terminal:

```
 * Serving Flask app 'url_shortener_api'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:105
 * Running on http://192.168.0.140:105
```
- The app exposes two endpoints:
    - `/encode` that accepts POST requests. You have to submit a request JSON object following this format: `{"url": "https://codesubmit.io/library/react"}`.
    - `/decode/<short_url_code>` that accepts GET requests.

### Sample requests
- You can try the `/encode` and `/decode` endpoints like the following:
- `curl -X POST http://127.0.0.1:105/encode -H 'Content-Type: application/json' -d '{"url": "https://codesubmit.io/library/react"}'`.
    - In case of success, the endpoint will return a JSON response like `{"encoded_url":"http://127.0.0.1:105/N6bba5"}`.
    - In case of failure, the endpoint will return a JSON response like `{"error":"The input argument is not a valid URL."}`.
- `curl http://127.0.0.1:105/decode/acbeJz`.
    - In case of success, the endpoint will return a JSON response like `{"decoded_url":"https://codesubmit.io/library/react"}`.
    - In case of failure, the endpoint will return a JSON response like `{"error":"No URL found for the input short URL code."}`.

### How to run the tests
- You can run the tests by running `pytest` in the root directory. This command will run all the tests created inside the `tests` directory.