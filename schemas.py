from typing import Union

from pydantic import BaseModel


class ChoiceBase(BaseModel):
    text: str

    class Config:
        orm_mode = True


class ChoiceIn(ChoiceBase):
    value: bool
    pass


class ChoiceOut(ChoiceBase):
    id: int



class QuestionBase(BaseModel):
    text: str
    class Config:
        orm_mode = True


class QuestionIn(QuestionBase):
    choices: list[ChoiceIn] = []


class QuestionOut(QuestionBase):
    id: int
    choices: list[ChoiceOut] = []