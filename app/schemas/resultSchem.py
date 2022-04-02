from pydantic import BaseModel
from .questionSchem import QuestionDetailOut
from .choiceSchem import ChoiceOut


class ResultBase(BaseModel):
    class Config:
        orm_mode = True


class ResultIn(ResultBase):
    """Result input display"""
    answer_id: int
    question_id: int


class AnswerOut(ChoiceOut):
    """The answer that was selected"""
    pass


class ResultOut(ResultBase):
    """Display of the  result """
    id: int
    answer_id: int
    question_id: int


class ResultDatailOut(ResultOut):
    """Full display of the  result """
    question: QuestionDetailOut
    choice: AnswerOut
