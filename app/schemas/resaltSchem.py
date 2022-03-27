from secrets import choice
from pydantic import BaseModel, Field
from .questionSchem import QuestionDetailOut
from .choiceSchem import  ChoiceOut


class ResaltBase(BaseModel):

    class Config:
        orm_mode = True


class ResaltIn(ResaltBase):
    answer_id: int
    question_id: int


class AnswerOut(ChoiceOut):
    pass

class ResaltOut(ResaltBase):
    id: int
    answer_id: int
    question_id: int
    question: QuestionDetailOut
    choice: AnswerOut  # = field alias