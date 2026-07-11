# fastapi-endpoint

## What it does
Exposes two JSON endpoints:

- `GET /health` — returns `{"status": "ok"}`
- `GET /greet` — returns a greeting message

## Running locally
Follow these steps to run on your Pc

## Running locally

Follow these steps to run on your PC

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Server runs at `http://127.0.0.1:8000`.

## Testing

Browser:
- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/greet

curl:
- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/greet
