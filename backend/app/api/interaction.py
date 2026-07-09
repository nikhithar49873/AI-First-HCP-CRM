from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database.connection import get_db
from app.schemas.interaction import (
    InteractionCreate,
    InteractionResponse,
)

from app.services.interaction_service import (
    create_interaction,
    get_all_interactions,
    get_interaction,
    update_interaction,
    delete_interaction
)

router = APIRouter(
    prefix="/interactions",
    tags=["Interactions"]
)


@router.post("/", response_model=InteractionResponse)
def add_interaction(
    interaction: InteractionCreate,
    db: Session = Depends(get_db)
):
    return create_interaction(db, interaction)
@router.get("/", response_model=List[InteractionResponse])
def get_interactions(
    db: Session = Depends(get_db)
):
    return get_all_interactions(db)


@router.get("/{interaction_id}",
            response_model=InteractionResponse)
def get_single_interaction(
    interaction_id: int,
    db: Session = Depends(get_db)
):
    return get_interaction(
        db,
        interaction_id
    )


@router.put("/{interaction_id}",
            response_model=InteractionResponse)
def edit_interaction(
    interaction_id: int,
    interaction: InteractionCreate,
    db: Session = Depends(get_db)
):

    return update_interaction(
        db,
        interaction_id,
        interaction
    )


@router.delete("/{interaction_id}")
def remove_interaction(
    interaction_id: int,
    db: Session = Depends(get_db)
):

    delete_interaction(
        db,
        interaction_id
    )

    return {
        "message": "Interaction deleted successfully"
    }