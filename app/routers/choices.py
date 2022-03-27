from fastapi import APIRouter, Depends #, HTTPException
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..schemas.choiceSchem import ChoiceOut, ChoiceIn, ChoiceQuestionId
from ..service import crud_choice


router = APIRouter(
    prefix="/coice",
    tags=["Coice"],
)

@router.post("/", response_model=ChoiceOut) ####
def create_choice(choice: ChoiceQuestionId , db: Session = Depends(get_db)):
    """Creating an answer for a question"""
    choice_dict =choice.dict()
    question_id = choice_dict['question_id']
    del choice_dict['question_id']
    choice = ChoiceIn(**choice_dict)
    return crud_choice.create_choice_for_question(db=db, choice=choice ,question_id=question_id)

@router.get("/{id}/",response_model=ChoiceQuestionId)
def read_choice(id: int , db: Session = Depends(get_db)):
    """Getting a specific answer"""
    choice = crud_choice.get(db,id=id)
    return choice


@router.put("/{id}/", response_model=ChoiceOut)
def update_choice(id: int, choice: ChoiceIn, db: Session = Depends(get_db)):
    """Answer update"""
    return crud_choice.update(db, id=id, obj_in=choice) 


@router.delete("/{id}/")
def delete_choice(id: int,db: Session = Depends(get_db)):
    """Delete answer"""
    return crud_choice.remove(db, id=id)