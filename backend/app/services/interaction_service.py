from sqlalchemy.orm import Session
from app.models.interaction import Interaction
from app.schemas.interaction import InteractionCreate


def create_interaction(db: Session, interaction: InteractionCreate):

    new_interaction = Interaction(
        doctor_name=interaction.doctor_name,
        hospital=interaction.hospital,
        specialization=interaction.specialization,
        interaction_date=interaction.interaction_date,
        interaction_type=interaction.interaction_type,
        discussion=interaction.discussion,
        products=interaction.products,
        follow_up_date=interaction.follow_up_date,
        notes=interaction.notes
    )

    db.add(new_interaction)

    db.commit()

    db.refresh(new_interaction)

    return new_interaction
def get_all_interactions(db: Session):
    return db.query(Interaction).all()


def get_interaction(db: Session, interaction_id: int):
    return db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()


def update_interaction(
    db: Session,
    interaction_id: int,
    interaction: InteractionCreate
):
    existing = db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()

    if existing:

        existing.doctor_name = interaction.doctor_name
        existing.hospital = interaction.hospital
        existing.specialization = interaction.specialization
        existing.interaction_date = interaction.interaction_date
        existing.interaction_type = interaction.interaction_type
        existing.discussion = interaction.discussion
        existing.products = interaction.products
        existing.follow_up_date = interaction.follow_up_date
        existing.notes = interaction.notes

        db.commit()
        db.refresh(existing)

    return existing


def delete_interaction(
    db: Session,
    interaction_id: int
):

    interaction = db.query(
        Interaction
    ).filter(
        Interaction.id == interaction_id
    ).first()

    if interaction:
        db.delete(interaction)
        db.commit()

    return interaction