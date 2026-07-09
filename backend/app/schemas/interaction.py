from pydantic import BaseModel
from datetime import date
from typing import Optional


class InteractionBase(BaseModel):
    doctor_name: str
    hospital: str
    specialization: str
    interaction_date: date
    interaction_type: str
    discussion: str
    products: str
    follow_up_date: date
    notes: Optional[str] = None


class InteractionCreate(InteractionBase):
    pass


class InteractionResponse(InteractionBase):
    id: int

    class Config:
        from_attributes = True