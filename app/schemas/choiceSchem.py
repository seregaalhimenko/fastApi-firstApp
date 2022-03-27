from typing import Optional
from pydantic import BaseModel

class ChoiceBase(BaseModel):
    text: str
    class Config:
        orm_mode = True

class ChoiceIn(ChoiceBase):
    value: bool
    owner_id :Optional[int] = None

class ShortChoiceIn(ChoiceBase):
    value: bool
    
class ChoiceOut(ChoiceBase):
    id: int

    