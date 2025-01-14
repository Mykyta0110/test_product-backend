
import re 
import uuid

from fastapi import HTTPException
from pydantic import BaseModel, field_validator
from typing import Optional
from pydantic import constr



class ShowProduct(BaseModel):
    id: int
    name: str
    price: int
    discount: Optional[int] = None
    
    class Config:
        orm_mode=True
        from_attributes=True
