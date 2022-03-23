from fastapi import Depends, FastAPI, Body
from sqlalchemy.orm import Session
from pydantic import Field
import models
import crud 
import schemas 
import service
from core.db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/create/question/", response_model=schemas.QuestionOut)
def create_question(question: schemas.QuestionIn, choices :list[schemas.ChoiceIn] = Body(...), db: Session = Depends(get_db)):
    """ Сreating a question with one or more answers."""
    return service.crud_question.create(db=db, question=question,choices=choices)


@app.get("/question_list/", response_model=list[schemas.QuestionOut])
def read_questions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Getting a list of questions"""
    questions = service.crud_question.get_multi(db, skip=skip, limit=limit)
    return questions


@app.get("/get_question/{question_id}/", response_model=schemas.QuestionDetailOut)
def read_question( question_id: int , db: Session = Depends(get_db)):
    """Getting a specific question"""
    questions = service.crud_question.get(db, id=question_id)
    return questions


@app.put("/question/{id}/", response_model=schemas.QuestionOut)
def update_question(id: int, question: schemas.QuestionIn, db: Session = Depends(get_db)):
   """Question update"""
   return service.crud_question.update(db, id=id, obj_in = question)


@app.delete("/question/{question_id}/")
def delete_question(question_id: int,db: Session = Depends(get_db)):
    """Delete question and answers"""
    return service.crud_question.remove(db, id=question_id)


@app.post("/create/choice/", response_model=schemas.ChoiceOut)
def create_choice(choice: schemas.ChoiceQuestionId , db: Session = Depends(get_db)):
    """Creating an answer for a question"""
    choice_dict =choice.dict()
    question_id = choice_dict['question_id']
    del choice_dict['question_id']
    choice = schemas.ChoiceIn(**choice_dict)
    return service.crud_choice.create_choice_for_question(db=db, choice=choice ,question_id=question_id)

@app.get("/choice/{id}/",response_model=schemas.ChoiceQuestionId)
def read_choice(id: int , db: Session = Depends(get_db)):
    """Getting a specific answer"""
    choice = service.crud_choice.get(db,id=id)
    return choice


@app.put("/choice/{choice_id}/", response_model=schemas.ChoiceOut)
def update_choice(choice_id: int, choice: schemas.ChoiceIn, db: Session = Depends(get_db)):
    """Answer update"""
    return service.crud_choice.update(db, id=choice_id, obj_in=choice) 


@app.delete("/choice/{choice_id}/")
def delete_choice(choice_id: int,db: Session = Depends(get_db)):
    """Delete answer"""
    return service.crud_choice.remove(db, id=choice_id)
