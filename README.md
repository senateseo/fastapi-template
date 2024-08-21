# Python Virtual Environment

```
python3 -m venv env
source env/bin/activate

```

# 1. Installation

### Install FastAPI

```
python -m pip install fastapi
```

### Install `uvicorn`

Uvicorn is an ASGI web server implementation for Python. Here's more detail. [Here](https://www.uvicorn.org/)

```
pip install uvicorn
```

### Run the server

```
uvicorn myapi:app
```

# 2. Testing Environment

`httpx` allows you to test HTTP Request and response.

### Install `httpx`

```
pip install httpx
```

### Install `pytest`

```
pip install pytest
```

### Run Test

```
pytest
```
