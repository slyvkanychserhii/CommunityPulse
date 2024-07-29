from pydantic import BaseModel, Field
from typing import Optional


class CategoryBase(BaseModel):
    id: Optional[int] = None
    name: str

    class Config:
        from_attributes = True
