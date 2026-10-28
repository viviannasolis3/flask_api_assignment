# flask_api_assignment

This project demonstrates a basic REST API built with Python 3 and Flask. It uses functions, if/else logic, dictionaries, lists, JSON responses, input validation, and HTTP status codes.

## Files

- `app.py` — Flask server and two endpoints
- `test_app.py` — eight automated tests using pytest
- `README.md` — setup and testing instructions

## Setup (Windows / Anaconda Prompt)

```bat
mkdir flask_api_assignment
cd flask_api_assignment
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install Flask pytest
```

Place `app.py` and `test_app.py` in the project folder. On macOS/Linux, activate the virtual environment with `source venv/bin/activate` instead.

## Run the server

```bat
python app.py
```

The development server runs at `http://127.0.0.1:5000`.

## Endpoints and expected outcomes

### GET /hello

Open `http://127.0.0.1:5000/hello` in a browser.

Expected HTTP 200 response:

```json
{"message": "Hello, World!"}
```

Open `http://127.0.0.1:5000/hello?name=Vivianna` for a personalized response:

```json
{"message": "Hello, Vivianna!"}
```

### POST /sum

In a second Anaconda Prompt window, run:

```bat
curl.exe -X POST http://127.0.0.1:5000/sum -H "Content-Type: application/json" -d "{\"numbers\":[1,2,3]}"
```

Expected HTTP 200 response:

```json
{"numbers": [1, 2, 3], "sum": 6}
```

If `numbers` is missing, empty, not a list, or contains non-numeric values, the API returns HTTP 400 with an error message. Malformed JSON and non-JSON requests also return HTTP 400.

## Run automated tests

In the project folder, with the virtual environment active:

```bat
python -m pytest test_app.py -v
```

Expected result: **8 passed**. These tests cover normal greetings, personalized greetings, valid sums, missing fields, mixed-type lists, empty lists, malformed JSON, and non-JSON requests. Record the actual result after running the command locally.

## Notes

- Python 3.x is required.
- The server uses port 5000 and starts with `python app.py`.
- The built-in Flask server is for local development and testing, not production deployment.
- Do not upload the `venv` folder to GitHub.
