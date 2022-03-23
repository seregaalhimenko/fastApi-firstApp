from random import choices
from typing import Union
# from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import update
from fastapi.encoders import jsonable_encoder

import schemas
import models


def get_detail_question(db: Session, question_id: int):
    return db.query(models.Question).filter(models.Question.id == question_id).first()


def get_questions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Question).offset(skip).limit(limit).all()


def create_choice(db: Session, choice: schemas.ChoiceIn, question_id: int):
    """Creating answer."""
    db_choice = models.Choice(**choice.dict(), owner_id=question_id)
    db.add(db_choice)
    db.commit()
    db.refresh(db_choice)
    return db_choice



def create_list_choice(db: Session, choices: list[schemas.ChoiceIn], question_id: int):
    print(choices)
    """Creating multiple answers."""
    for choice in choices:
        create_choice(db, choice, question_id)
    return get_detail_question(db,question_id)


def create_question(db: Session, question: schemas.QuestionIn, choices :list[schemas.ChoiceIn]):
    """ Сreating a question with one or more answers."""
    question_dict = question.dict()
    db_question = models.Question(**question_dict)
    db.add(db_question)
    db.commit()
    if choices:
        return create_list_choice(db,choices=choices,question_id=db_question.id)
    db.refresh(db_question)    
    return db_question


def get_choice_for_question(db: Session, question_id: int):
    return db.query(models.Choice).filter(models.Choice.owner_id == question_id).all()

def update_choice(db: Session, choice_id: int, сhoice: schemas.ChoiceIn):
    # сhoice_model = models.Choice.delete().where(models.Choice.id == choice_id)
    сhoice_model  = update(models.Choice).where(models.Choice.id == choice_id).values(**сhoice.dict())
    db.add(сhoice_model)
    db.commit()
    db.refresh(сhoice_model)
    return сhoice_model


# def update(db_session: Session, *, db_obj: models.Choice, obj_in: schemas.ChoiceIn) ->models.Choice:
#     obj_data = jsonable_encoder(db_obj)
#     update_data = obj_in.dict(skip_defaults=True)
#     for field in obj_data:
#         if field in update_data:
#             setattr(db_obj, field, update_data[field])
#     db_session.add(db_obj)
#     db_session.commit()
#     db_session.refresh(db_obj)
#     return db_obj