# fastapi_app.py
from fastapi import FastAPI, Depends
from main import login
from models import LoginData

app = FastAPI()


@app.post("/login/")
async def api_login(data: LoginData):
    return {"message": login(data.username, data.password)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=7861)
