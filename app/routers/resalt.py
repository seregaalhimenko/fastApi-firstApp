from urllib import request
from fastapi import APIRouter, Depends #, HTTPException
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..service import crud_resalt
from ..schemas.resaltSchem import  ResaltIn,  ResaltOut #,Answer, AnswersToQuestion

router = APIRouter(
    prefix="/resalt",
    tags=["Resalt"],
)

@router.post("/")
def create_resalt(request: ResaltIn, db:Session = Depends(get_db)):
    return crud_resalt.create(db, obj_in= request)


@router.get("/{id}/")
def read_resalt(id: int, db: Session = Depends(get_db)):
    return crud_resalt.get(db_session=db, id=id)

@router.get("/", response_model=list[ResaltOut])
def read_list_resalt(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_resalt.get_multi(db_session=db,skip=skip,limit=limit)


@router.put("/{id}")
def update_resalt(id: int,request: ResaltIn, db: Session = Depends(get_db)):
    return crud_resalt.update(db_session=db, id=id, obj_in=request)

@router.delete("/{id}")
def delete_resalt(id: int, db: Session =Depends(get_db)):
    return crud_resalt.remove(db_session=db,id=id)








    # return crud_question.results_on_questions(db,id)        ##########

# @router.get("/test/{id}/",response_model=AnswersToQuestion)
# def resalttest(id: int, db: Session = Depends(get_db)):
#     res_obj: Resalt = db.query(Resalt).filter(Resalt.id == id).first()
#     list_answ = db.query(Resalt.answer).filter(Resalt.question_id == res_obj.question_id).all()
#     AnswersToQuestion(question=res_obj.question,answers=list_answ)
#     return crud_resalt.get(db_session=db, id=id)

# @router.get("/list/",response_model=list(Answer))
# def resalt_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):   #?????
#     return crud_resalt.get_multi(db_session=db, skip=skip, limit=limit)


 

# @router.get("/resalt_all/", response_model=list[ResaltOut])
# def read_resalt_all(request, db:Session = Depends(get_db)):
#     print(request)
#     return db.query(models.Resalt).all()
# @router.get("/resalt_q/{id}", response_model=AnswersToQuestion)
# def read_resalt_all(id: int, db:Session = Depends(get_db)):
#     ques = db.query(Question).filter(Question.id == id).first()
#     # choices_and_answers = db.query(Resalt.answer_id, Resalt.answer_value,Choice.text,Choice.value).filter(Resalt.question_id == id).join(Choice, Resalt.answer_id == Choice.id).all()
#     castom_res_box : list(CastomResalt) = choices_and_answers
#     response = CastomResalt2(question_id=ques.id, question_text=ques.text,ans=castom_res_box)
#     return response