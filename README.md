# Techcombank's Homework: Creating RestAPI

## Technical Details
- The repo consists of one main.py for the API, written using Flask, and the "tests" folder containing some tests, written using pytest.
- Since this is a simple API for testing, I have opted not to use an app factory and blueprints.
- The main idea of the quantile calculation is to sort the pool values first, then using a formula (as libraries are not allowed). As the number of values in the pools grows however, sorting will get more computationally expensive and thus will have poorer scalability (at which point a library may be considered).
- The data is stored "locally" as a dictionary and will be wiped on every new session/instance of the app. Another alternative, should the data be kept, is to write to a local file. As the data size grows, that is when a database can be connected for more availability & computational speed.
- The "results" folder contains the testing results, as well as the queries when run on Postman.

### Tech stack

- API: Flask (Python)
- Testing: pytest

### How to start and use the API

1. Create virtual environment & install libs:

```
python -m venv venv
venv/Scripts/activate - for Window
pip install -r requirements.txt
```

2. Start Flask:

```
flask run
```

3. Send the POST/GET requests (with JSONs) to the API endpoint "/api/pools"

4. To run all the tests:

```
pytest
```