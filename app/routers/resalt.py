from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from ..dependencies import get_db, output_schema_definition
from ..service import crud_resalt, read_resalt_for_question

from ..schemas.resaltSchem import ResaltIn, ResaltOut, ResaltDatailOut
from ..schemas.answerSchem import AnswerListAndQuestion


router = APIRouter(
    prefix="/resalt",
    tags=["Resalt"],
)


@router.post("/", status_code=201)
def create_resalt(request: ResaltIn, db: Session = Depends(get_db)):
    """Сreating a result"""
    obj = crud_resalt.create(db, obj_in=request)
    return JSONResponse(status_code=201, headers={"Location": "/choice/{}/".format(obj.id)})


@router.get("/{id}/")
def read_resalt(id: int, db: Session = Depends(get_db), detail_mode: bool = False):
    """Getting a specific result
        params: detail_mode
        by default fasle if set to true there will be a verbose output of the result
    """
    res = crud_resalt.get(db_session=db, id=id)
    return output_schema_definition(ResaltDatailOut, ResaltOut, predicate=detail_mode, query=res)


@router.get("/")
def read_list_resalt(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Getting a list of result"""
    return crud_resalt.get_multi(db_session=db, skip=skip, limit=limit)


@router.put("/{id}")
def update_resalt(id: int, request: ResaltIn, db: Session = Depends(get_db)):
    """Result update"""
    return crud_resalt.update(db_session=db, id=id, obj_in=request)


@router.delete("/{id}", status_code=204)
def delete_resalt(id: int, db: Session = Depends(get_db)):
    """Result delete"""
    crud_resalt.remove(db_session=db, id=id)
    return JSONResponse(status_code=204)


@router.get("/question/{question_id}/", response_model=AnswerListAndQuestion)
def resalt_for_question(id: int, db: Session = Depends(get_db)):
    """ Result for a specific question """
    return read_resalt_for_question(db=db, question_id=id)
