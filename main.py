from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI(title="US Population")


@app.get("/")
async def welcome() -> dict:
    return FileResponse("index.html")
