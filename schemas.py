from typing import Optional

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


class QuestionBase(BaseModel):
    text: str
    class Config:
        orm_mode = True


class QuestionIn(QuestionBase):
    pass

class QuestionOut(QuestionBase):
    id: int

class QuestionDetailOut(QuestionOut):
    choices: list[ChoiceOut] = []