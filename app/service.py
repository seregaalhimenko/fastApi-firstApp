from sqlalchemy.orm import Session, Query
from fastapi import  HTTPException


from .schemas.questionSchem import  QuestionIn
from .schemas.questionSchem import  QuestionIn as QuestionUpdate
from .schemas.choiceSchem import ChoiceIn
from .schemas.choiceSchem import ChoiceIn as ChoiceInUpdate
from .schemas.resaltSchem import ResaltIn
from .schemas.answerSchem import AnswerListAndQuestion


from .models import Question, Choice, Resalt
from .base_crud import CRUDBase


class CRUDQuestion(CRUDBase[Question, QuestionIn, QuestionUpdate]):


    def __create_choice(self, db: Session, choice: ChoiceIn, question_id: int):
        """Creating answer."""
        db_choice = Choice(**choice.dict(), owner_id=question_id)
        db.add(db_choice)
        db.commit()
        db.refresh(db_choice)
        return db_choice

    def __create_list_choice(self, db: Session, choices: list[ChoiceIn], question_id: int):
        """Creating multiple answers."""
        for choice in choices:
            self.__create_choice(db, choice, question_id)
        return self.get(db,question_id)

    def create(
        self,
        db: Session,
        question: QuestionIn,
        choices :list[ChoiceIn]
        ):

        """ Сreating a question with one or more answers."""
        
        question_dict = question.dict()
        db_question = Question(**question_dict)
        db.add(db_question)
        db.commit()
        if choices:
            return self.__create_list_choice(db,choices=choices, question_id=db_question.id)
        db.refresh(db_question)    
        return db_question


class CRUDChoice(CRUDBase[Choice, ChoiceIn, ChoiceInUpdate]):
    def create_choice_for_question(
        self,
        db: Session,
        choice: ChoiceIn,
        question_id: int
        ):
        """Creating answer."""
        obj = db.get(Question, question_id)
        if not obj:
            raise HTTPException(
                status_code=404, 
                detail="question_id not found"
                )
        db_choice = Choice(**choice.dict(), owner_id=question_id)
        db.add(db_choice)
        db.commit()
        db.refresh(db_choice)
        return db_choice


    def create_list_choice(
        self,
        db: Session,
        choices: list[ChoiceIn],
        question_id: int
        ):
        """Creating multiple answers."""
        for choice in choices:
            self.create_choice_for_question(db, choice, question_id)
        return crud_question.get(db,question_id)


class CRUDResalt(CRUDBase[Resalt,ResaltIn,ResaltIn]):
    pass


def _result_handler(db:Session, question_id: int) ->Query:
    """выбранные ответы на вопрос"""
    return db.query(
        Resalt.answer_id, 
        Choice.text,
        Choice.value
        ).filter(
            Resalt.question_id == question_id
            ).join(
                Choice, Resalt.answer_id == Choice.id
                ).all()


def read_resalt_for_question(
        db:Session,
        question_id: int,
    ):
    ques = db.query(Question).filter(Question.id == question_id).first()
    list_answer = _result_handler(db,question_id=question_id)
    response = AnswerListAndQuestion(question = ques,answers=list_answer)
    return response


crud_question: CRUDQuestion = CRUDQuestion(Question)
crud_choice: CRUDChoice = CRUDChoice(Choice)
crud_resalt: CRUDResalt = CRUDResalt(Resalt)


