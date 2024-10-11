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


class AdditionInput(BaseModel):
    number1: float
    number2: float


@app.post("/add")
async def add_numbers(input_data: AdditionInput):
    total = input_data.number1 + input_data.number2
    return {"result": int(total)}
