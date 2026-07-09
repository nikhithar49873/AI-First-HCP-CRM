from fastapi import FastAPI
from app.database.connection import engine

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to AI-First HCP CRM Backend",
        "database": "Connected Successfully"
    }