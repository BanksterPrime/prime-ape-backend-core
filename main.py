from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Prime Ape Backend Core is live"}

class InputData(BaseModel):
    message: str

@app.post("/process")
def process_data(data: InputData):
    return {
        "received": data.message,
        "length": len(data.message),
        "service": "prime-ape-backend-core"
    }
