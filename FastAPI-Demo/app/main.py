from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


class DataModel(BaseModel):
    data: int


@app.post("/data")
async def data(request: DataModel):
    if request.data == 1:
        return {"message": "success"}
    elif request.data == 0:
        return {"message": "failure"}
    else:
        raise HTTPException(status_code=400, detail="Invalid data value")
