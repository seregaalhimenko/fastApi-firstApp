from pydantic import BaseModel

from .resaltSchem import ResaltOut 
from .choiceSchem import ChoiceOut

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