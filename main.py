from fastapi import FastAPI
from listener import listener

app = FastAPI()


app.include_router(listener)

@app.get("/")
def homepage():
    return {"msg" : "Welcome To the homepage of CICD test APP."}


@app.get("/cicd")
def cicd_test():
    return {"msg" : "Display of this msg means success of the CICD pipeline"}