from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from core.exceptions import AppException
from core.handlers import app_error_handler

app = FastAPI()
app.add_exception_handler(AppException, app_error_handler)
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/success/")
async def success(request: Request):
    return {"message": "Success"}

@app.post("/error/")
async def failure(request: Request):
    raise AppException("Error Replicated", 500)