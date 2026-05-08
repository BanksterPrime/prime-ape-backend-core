from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Prime Ape Backend Core is live"}
