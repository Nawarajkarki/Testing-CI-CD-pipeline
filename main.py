from fastapi import FastAPI
from listener import listener

app = FastAPI()


app.include_router(listener)

@app.get("/")
def homepage():
    return {"msg" : "Welcome To the homepage of CICD test APP."}