from pydantic import BaseModel

from .questionSchem import QuestionDetailOut


class Answer(BaseModel):
    answer_id: int
    text: str
    value: bool

    class Config:
        orm_mode = True


class AnswerListAndQuestion(BaseModel):
    question: QuestionDetailOut
    answers: list[Answer] = None
