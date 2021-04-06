from fastapi import FastAPI

app = FastAPI()


@app.post("/data")
async def root(param):
    return {"message": "Hello World " + param}

