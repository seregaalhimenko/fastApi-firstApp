from typing import Optional
from pydantic import BaseModel

class ChoiceBase(BaseModel):
    text: str
    class Config:
        orm_mode = True

class ChoiceIn(ChoiceBase):
    """Display input with question id"""
    value: bool
    owner_id :Optional[int] = None

class ShortChoiceIn(ChoiceBase):
    """Display input without question id"""
    value: bool 
    
class ChoiceOut(ChoiceBase):
    """Display output without value"""
    id: int

class ChoiceOutWithValue:
    """Display output with value"""
    value: bool 