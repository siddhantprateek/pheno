from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def base():
    return {"message": "Welcome to Pheno!"}


@app.get("/weather")
def get_weather(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}