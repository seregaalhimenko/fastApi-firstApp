from random import choices
from typing import Union
# from typing import Optional
from sqlalchemy.orm import Session

import schemas
import models


def get_question(db: Session, question_id: int):
    return db.query(models.Question).filter(models.Question.id == question_id).first()


def get_questions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Question).offset(skip).limit(limit).all()


def create_list_choice(db: Session, choices: list[schemas.ChoiceIn], question_id: int):
    print(choices)
    """Creating multiple answers."""
    for choice in choices:
        db_choice = models.Choice(**choice.dict(), owner_id=question_id)
        db.add(db_choice)
        db.commit()
    db.refresh(db_choice)
    return get_choice_for_question(db,question_id)


def create_question(db: Session, question: schemas.QuestionIn):
    """ Сreating a question with one or more answers."""
    question_dict = question.dict()
    db_question = models.Question(**question_dict)
    db.add(db_question)
    db.commit()
    choices: list[schemas.ChoiceIn] = question_dict['choices']
    if choices:
        return create_list_choice(db,choices=choices,question_id=db_question.id)
    db.refresh(db_question)    
    return db_question


def get_choice_for_question(db: Session, question_id: int):
    return db.query(models.Choice).filter(models.Choice.owner_id == question_id).all()

def get_choices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Choice).offset(skip).limit(limit).all()


def create_choice(db: Session, choice: schemas.ChoiceIn, question_id: int):
    db_choice = models.Choice(**choice.dict(), owner_id=question_id)
    db.add(db_choice)
    db.commit()
    db.refresh(db_choice)
    return db_choice

