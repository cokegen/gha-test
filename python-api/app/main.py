"""This is the app message"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_main():
    """This is the main message"""
    return {"msg": "Hello World 5"}


@app.get("/another")
async def read_another():
    """This is the alternate message"""
    return {"msg": "ANOTHER World"}
