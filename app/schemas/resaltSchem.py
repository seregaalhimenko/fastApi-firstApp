from secrets import choice
from pydantic import BaseModel, Field
from .questionSchem import QuestionDetailOut
from .choiceSchem import  ChoiceOut


class ResaltBase(BaseModel):
    class Config:
        orm_mode = True


class ResaltIn(ResaltBase):
    """Result input display"""
    answer_id: int
    question_id: int


class AnswerOut(ChoiceOut):
    """The answer that was selected"""
    pass

class ResaltOut(ResaltBase):
    """Full display of the  result """
    id: int
    answer_id: int
    question_id: int
    question: QuestionDetailOut
    choice: AnswerOut  # = field alias