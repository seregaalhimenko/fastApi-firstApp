from fastapi import Depends, FastAPI, HTTPException, Body
from sqlalchemy.orm import Session
from pydantic import Field
import models
import crud 
import schemas 

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
    return crud.create_question(db=db, question=question,choices=choices)


@app.get("/question_list/", response_model=list[schemas.QuestionOut])
def read_questions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    questions = crud.get_questions(db, skip=skip, limit=limit)
    return questions


@app.get("/get_question/{question_id}/", response_model=schemas.QuestionDetailOut)
def read_questions( question_id: int , db: Session = Depends(get_db)):
    questions = crud.get_detail_question(db, question_id)
    return questions


@app.post("/create/choice/", response_model=schemas.ChoiceOut)
def create_choice(choice: schemas.ChoiceQuestionId , db: Session = Depends(get_db)):
    choice_dict =choice.dict()
    question_id = choice_dict['question_id']
    del choice_dict['question_id']
    choice = schemas.ChoiceIn(**choice_dict)
    return crud.create_choice(db=db, choice=choice ,question_id=question_id)

@app.put("/choice/{choice_id}", response_model=schemas.ChoiceOut)
async def update_choice(choice_id: int, choice: schemas.ChoiceIn, db: Session = Depends(get_db)):
   return crud.update_choice(db,choice_id,choice)

@app.put("/2choice/{choice_id}", response_model=schemas.ChoiceOut)
async def update(choice_id: int, choice: schemas.ChoiceIn, db: Session = Depends(get_db)):
   return crud.update_choice(db,choice_id,choice) 