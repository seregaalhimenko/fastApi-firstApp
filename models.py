from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from core.db import Base


class Question(Base):
    """Model Question"""

    __tablename__ = "question"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text = Column(String)
    choices = relationship("Choice", back_populates="owner")


class Choice(Base):
    """Model Choice"""

    __tablename__ = "choice"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text = Column(String)
    value = Column(Boolean)
    owner_id = Column(Integer, ForeignKey("question.id"))
    owner = relationship("Question", back_populates="choices")