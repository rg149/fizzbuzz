# Fizz Buzz REST Server

## Overview
This is a production-ready Fizz-Buzz REST Server with Gunicorn as the WSGI server.

## Project Structure
The project follows a common Python project layout:

fizzbuzz_server/
|-- fizzbuzz/
| |-- init.py
| |-- app.py
| |-- wsgi.py
|-- tests/
| |-- init.py
| |-- test_fizzbuzz.py
|-- requirements.txt
|-- Dockerfile
|-- README.md


- **`fizzbuzz/`**: Application code.
- **`tests/`**: Unit tests.
- **`requirements.txt`**: Project dependencies.
- **`Dockerfile`**: Docker configuration.

## Getting Started

### Prerequisites
- [Docker](https://www.docker.com/)

### Build Docker Image
```bash
docker build -t fizzbuzz-server .
```

### Run Docker File
```bash
docker run -p 5000:5000 fizzbuzz-server
```

### Unit Tests
To run unit tests, execute:

```bash
python -m unittest discover -s tests
```

### Dependencies
Flask: Web framework. Being lightweight, Flask web framework has been preferred.
Gunicorn: WSGI server for making application production ready.

### API Documentation

API Documentation can be found [here](https://github.com/rg149/fizzbuzz/blob/main/API%20Guide.md)

