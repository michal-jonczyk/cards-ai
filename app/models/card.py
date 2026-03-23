from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base


class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    front = Column(String, nullable=False)
    back = Column(String, nullable=False)
    easiness = Column(Float, default=2.5)
    interval = Column(Integer,default=1)
    repetitions = Column(Integer, default=0)
    next_review = Column(DateTime(timezone=True),server_default=func.now())
    created_at = Column(DateTime(timezone=True),server_default=func.now())

    owner = relationship('User',back_populates='cards')