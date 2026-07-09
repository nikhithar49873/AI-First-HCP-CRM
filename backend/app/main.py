from fastapi import FastAPI

from app.database.connection import engine
from app.database.models import Base

from app.models.interaction import Interaction

from app.api.interaction import router as interaction_router

app = FastAPI(
    title="AI First HCP CRM"
)

Base.metadata.create_all(bind=engine)

app.include_router(interaction_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI First HCP CRM Backend"
    }