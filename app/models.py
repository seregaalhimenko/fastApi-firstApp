from secrets import choice
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from core.db import Base


class Question(Base):
    """Model Question"""

    __tablename__ = "question"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text = Column(String)

    choices = relationship(
        "Choice", cascade="all, delete-orphan", back_populates="owner")
    result = relationship(
        "Result", cascade="all, delete-orphan", back_populates="question")


class Choice(Base):
    """Model Choice"""

    __tablename__ = "choice"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text = Column(String)
    value = Column(Boolean)  # determines the correct choice or not
    owner_id = Column(Integer, ForeignKey("question.id"))

    owner = relationship("Question",  back_populates="choices")
    result = relationship("Result", back_populates="choice")


class Result(Base):
    """Model Result"""
    __tablename__ = "result"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    # Не совсем понимаю как строиться составной первичный ключ под капотом у orm
    # Сделать так, чтобы в базе не было одинаковых записей и не проверять перед добавлением строки в таблицу( возможно придется обработать исключение )
    question_id = Column(Integer, ForeignKey(
        "question.id"))  # primary_key=True
    answer_id = Column(Integer, ForeignKey("choice.id"))  # primary_key=True

    question = relationship("Question", back_populates="result")
    choice = relationship("Choice", back_populates="result")
