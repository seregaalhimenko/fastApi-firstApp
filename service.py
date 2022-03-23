from sqlalchemy.orm import Session
from schemas import  QuestionIn
from schemas import  QuestionIn as QuestionUpdate
from schemas import ChoiceIn
from schemas import ChoiceIn as ChoiceInUpdate
from models import Question, Choice
from base_crud import CRUDBase
from fastapi import  HTTPException

# def create_list_choice(db: Session, choices: list[ChoiceIn], question_id: int):#  жаль что не получилось !
#     """Creating multiple answers."""
#     for choice in choices:
#         CRUDChoice(Choice).create_choice_for_question(db, choice, question_id)
#     return CRUDQuestion(Question).get(db,question_id)

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




crud_question: CRUDQuestion = CRUDQuestion(Question)
crud_choice = CRUDChoice(Choice)
