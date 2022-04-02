from fastapi import APIRouter, Depends, Response, status
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from ..dependencies import get_db, output_schema_definition
from ..service import crud_result, read_result_for_question

from ..schemas.resultSchem import ResultIn, ResultOut, ResultDatailOut
from ..schemas.answerSchem import AnswerListAndQuestion


router = APIRouter(
    prefix="/result",
    tags=["Result"],
)


@router.post("/", status_code=201)
def create_result(request: ResultIn, db: Session = Depends(get_db)):
    """Сreating a result"""
    obj = crud_result.create(db, obj_in=request)
    return JSONResponse(status_code=201, headers={"Location": "/result/{}/".format(obj.id)})


@router.get("/{id}/")
def read_result(id: int, db: Session = Depends(get_db), detail_mode: bool = False):
    """Getting a specific result
        params: detail_mode
        by default fasle if set to true there will be a verbose output of the result
    """
    res = crud_result.get(db_session=db, id=id)
    return output_schema_definition(ResultDatailOut, ResultOut, predicate=detail_mode, query=res)


@router.get("/")
def read_list_result(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Getting a list of result"""
    return crud_result.get_multi(db_session=db, skip=skip, limit=limit)


@router.put("/{id}")
def update_result(id: int, request: ResultIn, db: Session = Depends(get_db)):
    """Result update"""
    return crud_result.update(db_session=db, id=id, obj_in=request)


@router.delete("/{id}", responses={204: {"model": None}})
def delete_result(id: int, db: Session = Depends(get_db)):
    """Result delete"""
    crud_result.remove(db_session=db, id=id)
    # такой способ чтоб исключить ошибку
    # h11._util.LocalProtocolError: Too much data for declared Content-Length h11._util.LocalProtocolError: Too much data for declared Content-Length
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/question/{question_id}/", response_model=AnswerListAndQuestion)
def result_for_question(id: int, db: Session = Depends(get_db)):
    """ Result for a specific question """
    return read_result_for_question(db=db, question_id=id)
