from cgitb import handler
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "true"}

@app.get("/ping")
def ping():
    return {"ping": "pong!!!"}

@app.get("/ping/pong")
def pingpong():
    return {"ping_pong": "wow"}

handler = Mangum(app)
