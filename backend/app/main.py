# backend/app/main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .api_router import router  # Ensure correct relative import

app = FastAPI()

app.include_router(router, prefix="/api")

app.mount("/", StaticFiles(directory="./dist", html=True), name="static")