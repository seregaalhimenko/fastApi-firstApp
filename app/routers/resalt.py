from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..service import crud_resalt
from ..schemas.resaltSchem import  ResaltIn,  ResaltOut

router = APIRouter(
    prefix="/resalt",
    tags=["Resalt"],
)

@router.post("/",status_code=201)
def create_resalt(request: ResaltIn, db:Session = Depends(get_db)):
    obj =  crud_resalt.create(db, obj_in= request)
    return JSONResponse(status_code=201,headers={"Location":"/choice/{}/".format(obj.id)})


@router.get("/{id}/")
def read_resalt(id: int, db: Session = Depends(get_db)):
    return crud_resalt.get(db_session=db, id=id)

@router.get("/")
def read_list_resalt(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_resalt.get_multi(db_session=db,skip=skip,limit=limit)


@router.put("/{id}")
def update_resalt(id: int,request: ResaltIn, db: Session = Depends(get_db)):
    return crud_resalt.update(db_session=db, id=id, obj_in=request)


@router.delete("/{id}", status_code=204)
def delete_resalt(id: int, db: Session =Depends(get_db)):
    return crud_resalt.remove(db_session=db,id=id)