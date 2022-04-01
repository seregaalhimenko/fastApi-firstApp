from core.db import SessionLocal

from sqlalchemy.orm import Query
from pydantic import BaseModel


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Позже попробовать сделать зависимость для fastAPI
def output_schema_definition(
    true_class_scheme: BaseModel,
    false_class_scheme: BaseModel,
    predicate: bool,
    query: Query
):
    if predicate:
        return true_class_scheme.from_orm(query)
    return false_class_scheme.from_orm(query)
