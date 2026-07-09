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