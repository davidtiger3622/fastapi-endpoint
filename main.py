from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/greet")
def greet():
    return {"message": "Hello Good start"}
