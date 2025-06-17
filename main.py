from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/success/")
async def success(request: Request):
    return {"message": "Success"}

@app.post("/error/")
async def failure(request: Request):
    return {"message": "Error"}