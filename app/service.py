from random import choices
from sqlalchemy.orm import Session, Query
from fastapi import HTTPException


from .schemas.questionSchem import QuestionIn, QuestionDetailIn
from .schemas.questionSchem import QuestionIn as QuestionUpdate
from .schemas.choiceSchem import ChoiceIn, ShortChoiceIn
from .schemas.choiceSchem import ChoiceIn as ChoiceInUpdate
from .schemas.resultSchem import ResultIn
from .schemas.answerSchem import AnswerListAndQuestion


from .models import Question, Choice, Result
from .base_crud import CRUDBase


class CRUDQuestion(CRUDBase[Question, QuestionIn, QuestionUpdate]):

    def __create_choice(self, db: Session, choice: dict, question_id: int):
        """Creating answer."""
        db_choice = Choice(**choice, owner_id=question_id)
        db.add(db_choice)
        db.commit()
        db.refresh(db_choice)
        return db_choice

    def __create_list_choice(self, db: Session, choices: list[ChoiceIn], question_id: int):
        """Creating multiple answers."""
        for choice in choices:
            self.__create_choice(db, choice, question_id)
        return self.get(db, question_id)

    def castom_create(
        self,
        db: Session,
        question: QuestionDetailIn,
    ):
        """ Сreating a question with one or more answers."""
        choices = question.dict()["choices"]
        question_dict = question.dict()
        del question_dict["choices"]
        db_question = Question(**question_dict)
        db.add(db_question)
        db.commit()
        if choices:
            return self.__create_list_choice(db, choices=choices, question_id=db_question.id)
        db.refresh(db_question)
        return db_question


class CRUDChoice(CRUDBase[Choice, ChoiceIn, ChoiceInUpdate]):
    def create_choice_for_question(
        self,
        db: Session,
        choice: ShortChoiceIn,
        question_id: int
    ) -> Choice:
        """Creating answer."""
        obj = db.get(Question, question_id)
        if not obj:
            raise HTTPException(
                status_code=404,
                detail=f"There is no question with id = {question_id}"
            )
        db_choice = Choice(**choice.dict(), owner_id=question_id)
        db.add(db_choice)
        db.commit()
        db.refresh(db_choice)
        return db_choice

    def create_list_choice(
        self,
        db: Session,
        choices: list[ShortChoiceIn],
        question_id: int
    ) -> Question:
        """Creating multiple answers."""
        for choice in choices:
            self.create_choice_for_question(db, choice, question_id)
        return crud_question.get(db, question_id)


class CRUDResult(CRUDBase[Result, ResultIn, ResultIn]):

    def create(self, db_session: Session, *, obj_in: ResultIn) -> Result:
        obj_in.answer_id
        obj_in.question_id
        question_obj = db_session.get(Question, obj_in.question_id)
        choice_obj = db_session.get(Choice, obj_in.answer_id)
        if not (question_obj and choice_obj):
            raise HTTPException(
                status_code=404,
                detail="Not found"
            )
        choice: Choice = db_session.get(Choice, obj_in.answer_id)
        if choice.owner_id != obj_in.question_id:
            raise HTTPException(
                status_code=404,
                detail=f"There is no such answer in the question"
            )
        return super().create(db_session, obj_in=obj_in)


def _result_handler(db: Session, question_id: int) -> Query:
    """выбранные ответы на вопрос"""
    return db.query(
        Result.answer_id,
        Choice.text,
        Choice.value
    ).filter(
        Result.question_id == question_id
    ).join(
        Choice, Result.answer_id == Choice.id
    ).all()


def read_result_for_question(
    db: Session,
    question_id: int,
):
    question_obj = db.get(Question, question_id)
    if not question_obj:
        raise HTTPException(
            status_code=404,
            detail=f"There is no question with id = {question_id}"
        )
    list_answer = _result_handler(db, question_id=question_id)
    response = AnswerListAndQuestion(
        question=question_obj, answers=list_answer)
    return response


crud_question: CRUDQuestion = CRUDQuestion(Question)
crud_choice: CRUDChoice = CRUDChoice(Choice)
crud_result: CRUDResult = CRUDResult(Result)
