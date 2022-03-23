from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from core.db import Base


class Question(Base):
    """Model Question"""

    __tablename__ = "question"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text = Column(String)
    choices = relationship("Choice", cascade="all, delete-orphan", back_populates="owner")


class Choice(Base):
    """Model Choice"""

    __tablename__ = "choice"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text = Column(String)
    value = Column(Boolean)
    owner_id = Column(Integer, ForeignKey("question.id"))
    owner = relationship("Question",  back_populates="choices")


# class Resalt(Base):
#     """Model Resalt"""
#     __tablename__ = "resalt"

#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     answer_id = Column(Integer, ForeignKey("choice.id"))
#     answer_text = Column(String, ForeignKey("choice.text"))
#     answer = relationship("Choice",  back_populates="resalts_choice")
#     question_id = Column(Integer, ForeignKey("question.id"))
#     question = relationship("Question",  back_populates="resalts_question")
#     answer_value = Column(Boolean)
