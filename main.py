from fastapi import FastAPI
from listener import listener

app = FastAPI()


app.include_router(listener)

@app.get("/github-actions")
def actions():
    return ("Github actions requirements installation check.")


@app.get("/")
def cicd_home():
    return {"msg" : "Should work"}


@app.get("/dependency")
def dependency():
    return {"msg" : "dependencies installation"}

@app.get("/cicd/{anything}")
def return_anything(anything:str):
    return {"msg" : "This indicates Success of the CICD pipeline implemented", "Your Msg" : f"{anything}"}


@app.get("/pm2-watch")
def checkpm2watch():
    return {"msg" : "indicates pm2 --watch works"}
    