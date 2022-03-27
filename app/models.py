from secrets import choice
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from core.db import Base


class Question(Base):
    """Model Question"""

    __tablename__ = "question"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text = Column(String)

    choices = relationship("Choice", cascade="all, delete-orphan", back_populates="owner")
    resalt = relationship("Resalt", cascade="all, delete-orphan", back_populates="question")



class Choice(Base):
    """Model Choice"""

    __tablename__ = "choice"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text = Column(String)
    value = Column(Boolean)
    owner_id = Column(Integer, ForeignKey("question.id"))

    owner = relationship("Question",  back_populates="choices")
    resalt = relationship("Resalt", back_populates="choice")




class Resalt(Base):
    """Model Resalt"""
    __tablename__ = "resalt"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey("question.id"))
    answer_id = Column(Integer, ForeignKey("choice.id"))

    question = relationship("Question", back_populates="resalt")
    choice = relationship("Choice", back_populates="resalt")