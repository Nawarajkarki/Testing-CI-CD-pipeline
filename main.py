from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def homepage():
    return {"msg" : "Welcome To the homepage"}