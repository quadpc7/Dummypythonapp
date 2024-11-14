# app.py

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Initialize FastAPI app
app = FastAPI()

# Set up Jinja2 templates for HTML rendering
templates = Jinja2Templates(directory="templates")

# API route to return a greeting message
@app.get("/greet/{name}")
async def greet(name: str):
    return {"message": f"Hello, {name}!"}

# Route for main HTML page
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
