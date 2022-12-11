import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Named Entity Recognition API")


@app.get("/")
def index():
    return {"Hello": "World!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
