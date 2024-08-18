from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.router import router as api_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(api_router)