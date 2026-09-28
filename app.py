from fastapi import FastAPI

app = FastAPI(title="Campus Pulse AI")

@app.get("/")
def read_root():
    return {"status": "online", "message": "Campus Pulse AI API is running!"}