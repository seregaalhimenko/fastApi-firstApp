from pydantic import BaseModel

# from .resaltSchem import ResaltOut  cicle
from .choiceSchem import ChoiceOut

class QuestionBase(BaseModel):
    text: str
    class Config:
        orm_mode = True


class QuestionIn(QuestionBase):
    """Display question model without id"""
    pass

class QuestionOut(QuestionBase):
    """Question model display"""
    id: int

class QuestionDetailOut(QuestionOut):
    """Displaying a question with all possible answers"""
    choices: list[ChoiceOut] = []