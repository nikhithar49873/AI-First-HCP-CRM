from fastapi import FastAPI

from app.database.connection import engine
from app.database.models import Base

# Import the Interaction model so SQLAlchemy knows about it
from app.models.interaction import Interaction

app = FastAPI(
    title="AI-First HCP CRM API"
)

# Create all database tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI-First HCP CRM Backend"
    }