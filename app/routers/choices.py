from fastapi import APIRouter, Depends #, HTTPException
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..schemas.choiceSchem import ChoiceOut, ChoiceIn
from ..schemas.questionSchem import QuestionDetailOut

from ..service import crud_choice


router = APIRouter(
    prefix="/choice",
    tags=["Choice"],
)

@router.post("/{question_id}",response_model=QuestionDetailOut, status_code=201) #### возвращает вопрос
def create_list_choice(choices: list[ChoiceIn], question_id: int, db: Session = Depends(get_db)):
    """Create answers to a question"""
    return crud_choice.create_list_choice(db=db, choices=choices ,question_id=question_id)


@router.post("/",status_code=201)
def create_choice(choice: ChoiceIn, db: Session = Depends(get_db)):
    """Create one answer per question"""
    return crud_choice.create(db_session=db, obj_in=choice)

@router.get("/{id}/",response_model=ChoiceIn)
def read_choice(id: int , db: Session = Depends(get_db)):
    """Getting a specific answer"""
    choice = crud_choice.get(db,id=id)
    return choice


@router.put("/{id}/", response_model=ChoiceOut)
def update_choice(id: int, choice: ChoiceIn, db: Session = Depends(get_db)):
    """Answer update"""
    return crud_choice.update(db, id=id, obj_in=choice) 


@router.delete("/{id}/", status_code=204)
def delete_choice(id: int,db: Session = Depends(get_db)):
    """Delete answer"""
    return crud_choice.remove(db, id=id)