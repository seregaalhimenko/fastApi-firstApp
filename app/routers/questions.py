from fastapi import Body, APIRouter, Depends #, HTTPException

from sqlalchemy.orm import Session
from app.dependencies import get_db

from app.schemas.questionSchem import QuestionOut, QuestionDetailOut, QuestionIn
from app.schemas.choiceSchem import ChoiceIn
from app.schemas.answerSchem import AnswerListAndQuestion

from app.service import crud_question, read_resalt_for_question

router = APIRouter(
    prefix="/question",
    tags=["Question"],
)

@router.post("/", response_model=QuestionDetailOut, status_code=201)
def create_question(question: QuestionIn, choices :list[ChoiceIn] = Body(...), db: Session = Depends(get_db)):
    """ Сreating a question with one or more answers."""
    return crud_question.create(db=db, question=question,choices=choices)


@router.get("/list/", response_model=list[QuestionOut])
def read_questions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Getting a list of questions"""
    questions = crud_question.get_multi(db, skip=skip, limit=limit)
    return questions


@router.get("/{id}/", response_model=QuestionDetailOut)
def read_question( id: int , db: Session = Depends(get_db)):
    """Getting a specific question"""
    questions = crud_question.get(db, id=id)
    return questions


@router.put("/{id}/")
def update_question(id: int, question: QuestionIn, db: Session = Depends(get_db)):
   """Question update"""
   return crud_question.update(db, id=id, obj_in = question)


@router.delete("/{id}/", status_code=204)
def delete_question(id: int,db: Session = Depends(get_db)):
    """Delete question and answers"""
    return crud_question.remove(db, id=id)

@router.get("/{id}/resalt", response_model=AnswerListAndQuestion)
def resalt(id: int, db: Session = Depends(get_db)):
    return read_resalt_for_question(db=db, question_id=id)