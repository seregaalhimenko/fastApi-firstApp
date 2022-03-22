from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

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

@app.post("/question/", response_model=schemas.QuestionOut)
def create_question(question: schemas.QuestionIn, db: Session = Depends(get_db)):
    return crud.create_question(db=db, question=question)



@app.get("/questions/", response_model=list[schemas.QuestionOut])
def read_questions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    questions = crud.get_questions(db, skip=skip, limit=limit)
    return questions
