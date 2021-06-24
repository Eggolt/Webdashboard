from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    x = {"message": "Hello WORLD!!! Welcome to FastAPI!!!"}
    return x
