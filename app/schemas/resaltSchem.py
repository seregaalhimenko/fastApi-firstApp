from pydantic import BaseModel
from .questionSchem import QuestionDetailOut
from .choiceSchem import ChoiceOut


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
    """Display of the  result """
    id: int
    answer_id: int
    question_id: int


class ResaltDatailOut(ResaltOut):
    """Full display of the  result """
    question: QuestionDetailOut
    choice: AnswerOut
