from pydantic import BaseModel

class ChoiceBase(BaseModel):
    text: str
    class Config:
        orm_mode = True

class ChoiceIn(ChoiceBase):
    value: bool

class ChoiceOut(ChoiceBase):
    id: int

class ChoiceQuestionId(ChoiceOut):
    owner_id :int 