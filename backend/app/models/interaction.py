from sqlalchemy import Column, Integer, String, Date
from app.database.models import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    doctor_name = Column(String(100))

    hospital = Column(String(100))

    specialization = Column(String(100))

    interaction_date = Column(Date)

    interaction_type = Column(String(50))

    discussion = Column(String(500))

    products = Column(String(255))

    follow_up_date = Column(Date)

    notes = Column(String(500))