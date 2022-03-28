
from typing import Optional, Generic, TypeVar, Type
from fastapi.encoders import jsonable_encoder
from fastapi import  HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from core.db import Base



ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, db_session: Session, id: int) -> Optional[ModelType]:
        obj = db_session.get(self.model, id)
        if not obj:
            raise HTTPException(                               
                status_code=404, 
                detail="{} not found".format(self.model.__name__)
                )
        return obj

    def get_multi(self, db_session: Session, *, skip=0, limit=100) -> list[ModelType]:
        return db_session.query(self.model).offset(skip).limit(limit).all()


    def update(
        self, db_session: Session, *,id: int, obj_in: UpdateSchemaType
) -> ModelType:
        db_obj = db_session.get(self.model, id)
        if not db_obj:
            raise HTTPException(
                status_code=404,
                detail="{} not found".format(self.model.__name__)
            )
        obj_data = obj_in.dict(exclude_unset=True)
        for key, value in obj_data.items():
            setattr(db_obj, key, value)
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return db_obj


    def remove(self, db_session: Session, *, id: int) -> ModelType:
        obj = db_session.get(self.model, id)
        if not obj:
            raise HTTPException(
                status_code=404, 
                detail="{} not found".format(self.model.__name__)
                )  
        db_session.delete(obj)
        db_session.commit()
        return {"ok": True}

    def create(self, db_session: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return db_obj   