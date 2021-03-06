from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..schemas.choiceSchem import ChoiceIn, ShortChoiceIn
from ..schemas.questionSchem import QuestionDetailOut

from ..service import crud_choice


router = APIRouter(
    prefix="/choice",
    tags=["Choice"],
)


@router.post("/{question_id}", response_model=QuestionDetailOut, status_code=201)
def create_list_choice(choices: list[ShortChoiceIn], question_id: int, db: Session = Depends(get_db)):
    """Create answers to a question"""
    return crud_choice.create_list_choice(db=db, choices=choices, question_id=question_id)


@router.post("/")
def create_choice(choice: ChoiceIn, db: Session = Depends(get_db)):
    """Create one answer per question"""
    obj = crud_choice.create(db_session=db, obj_in=choice)
    return JSONResponse(status_code=201, headers={"Location": "/choice/{}/".format(obj.id)})


@router.get("/{id}/", response_model=ChoiceIn)
def read_choice(id: int, db: Session = Depends(get_db)):
    """Getting a specific answer"""
    choice = crud_choice.get(db, id=id)
    return choice


@router.put("/{id}/")
def update_choice(id: int, choice: ChoiceIn, db: Session = Depends(get_db)):
    """Answer update"""
    return crud_choice.update(db, id=id, obj_in=choice)


@router.delete("/{id}/")
def delete_choice(id: int, db: Session = Depends(get_db)):
    """Delete answer"""
    crud_choice.remove(db, id=id)
    return JSONResponse(status_code=204)
