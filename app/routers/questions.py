from fastapi import Body, APIRouter, Depends 
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from app.dependencies import get_db

from app.schemas.questionSchem import QuestionOut, QuestionDetailOut, QuestionIn
from app.schemas.choiceSchem import ShortChoiceIn
from app.schemas.answerSchem import AnswerListAndQuestion

from app.service import crud_question, read_resalt_for_question

router = APIRouter(
    prefix="/question",
    tags=["Question"],
)

@router.post("/")
def create_question(question: QuestionIn, choices :list[ShortChoiceIn] = Body(...), db: Session = Depends(get_db)):
    """ Сreating a question with one or more answers."""
    obj = crud_question.create(db=db, question=question,choices=choices)
    return JSONResponse(status_code=201,headers={"Location":"/choice/{}/".format(obj.id)})


@router.get("/list/", response_model=list[QuestionOut])
def read_list_questions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Getting a list of questions"""
    questions = crud_question.get_multi(db, skip=skip, limit=limit)
    return questions


@router.get("/{id}/")
def read_question(id: int , db: Session = Depends(get_db), detail_mode: bool=False):
    """Getting a specific question
        params: detail_mode
        by default fasle if set to true there will be a verbose output of the question
    """
    question = crud_question.get(db, id=id)
    if detail_mode:
        scheme = QuestionDetailOut.from_orm(question)
        return scheme
    scheme = QuestionOut.from_orm(question)
    return scheme


@router.put("/{id}/",response_model=QuestionOut)
def update_question(id: int, question: QuestionIn, db: Session = Depends(get_db)):
   """Question update"""
   return crud_question.update(db, id=id, obj_in = question)


@router.delete("/{id}/")
def delete_question(id: int,db: Session = Depends(get_db)):
    """Delete question and answers"""
    crud_question.remove(db, id=id)
    return JSONResponse(status_code=204)

@router.get("/{id}/resalt", response_model=AnswerListAndQuestion) # убрать в резалт
def resalt(id: int, db: Session = Depends(get_db)):
    return read_resalt_for_question(db=db, question_id=id)
