# doggy-daycare

A basic Python 3.10 API.

## Setup

Requires [Python 3.10](https://www.python.org/downloads/).

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

The API is available at `http://127.0.0.1:8000`.

## Endpoints

| Method | Path | Response |
|--------|------|----------|
| GET | `/` | `{"message": "Hello, World!"}` |