from pydantic import BaseModel, Field
# from .questionSchem import QuestionOut
from .choiceSchem import ChoiceOut, ChoiceBase


class ResaltBase(BaseModel):

    class Config:
        orm_mode = True


class ResaltIn(ResaltBase):
    # answer_id: int
    question_id: int

class QuestionBbbb(BaseModel):
    id:int
    text: str
    class Config:
        orm_mode = True

        
class ResaltOut(ResaltBase):
    id: int
    answer_id: int
    question_id: int
    question: QuestionBbbb
    choice: list[ChoiceOut]=[]
    

# class ChoiseValue(ChoiceBase): # пока это ин
#     value: bool

# class Answer(BaseModel):
#     id: int
#     question: QuestionOut = Field(title="question")
#     # answers: list[Answer]
#     answer: ChoiseValue
#     class Config:
#         orm_mode = True


# # class AnswersToQuestion(BaseModel):
# #     question: QuestionOut #= Field(title="question")
# #     answers: list[Answer]
# #     # answer: Answer
# #     class Config:
# #         orm_mode = True

# class AnswersToQuestion(BaseModel):
#     question_id: int
#     answer: list[ChoiceOut]
#     class Config:
#         orm_mode = True