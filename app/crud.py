


# from random import choices
# from typing import Union
# # from typing import Optional
# from sqlalchemy.orm import Session
# from sqlalchemy import update
# # from fastapi.encoders import jsonable_encoder
# from fastapi import  HTTPException
# import schemas
# import models


# def get_detail_question(db: Session, question_id: int):
#     return db.query(models.Question).filter(models.Question.id == question_id).first()


# def get_questions(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Question).offset(skip).limit(limit).all()


# def create_choice(db: Session, choice: schemas.ChoiceIn, question_id: int):
#     """Creating answer."""
#     db_choice = models.Choice(**choice.dict(), owner_id=question_id)
#     db.add(db_choice)
#     db.commit()
#     db.refresh(db_choice)
#     return db_choice



# def create_list_choice(db: Session, choices: list[schemas.ChoiceIn], question_id: int):
#     """Creating multiple answers."""
#     for choice in choices:
#         create_choice(db, choice, question_id)
#     return get_detail_question(db,question_id)


# def create_question(db: Session, question: schemas.QuestionIn, choices :list[schemas.ChoiceIn]):
#     """ Сreating a question with one or more answers."""
#     question_dict = question.dict()
#     db_question = models.Question(**question_dict)
#     db.add(db_question)
#     db.commit()
#     if choices:
#         return create_list_choice(db,choices=choices,question_id=db_question.id)
#     db.refresh(db_question)    
#     return db_question


# def get_choice_for_question(db: Session, question_id: int):
#     return db.query(models.Choice).filter(models.Choice.owner_id == question_id).all()



# def update_choice(db: Session, choice_id: int, choice: schemas.ChoiceIn):
#     db_choice = db.get(models.Choice, choice_id)
#     if not db_choice:
#         raise HTTPException(status_code=404, detail="Choice not found")
#     choice_data = choice.dict(exclude_unset=True)
#     for key, value in choice_data.items():
#         setattr(db_choice, key, value)
#     db.add(db_choice)
#     db.commit()
#     db.refresh(db_choice)
#     return db_choice


# def update_question(db: Session, question_id: int, question: schemas.QuestionIn):
#     db_question = db.get(models.Question, question_id)
#     if not db_question:
#         raise HTTPException(status_code=404, detail="Question not found")
#     question_data = question.dict(exclude_unset=True)
#     for key, value in question_data.items():
#         setattr(db_question, key, value)
#     db.add(db_question)
#     db.commit()
#     db.refresh(db_question)
#     return db_question

    
# def delete_question(db: Session,question_id: int):
#         question = db.get(models.Question, question_id)
#         if not question:
#             raise HTTPException(status_code=404, detail="Question not found")
#         db.delete(question)
#         db.commit()
#         return {"ok": True}
