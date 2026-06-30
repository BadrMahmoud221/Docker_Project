from pydantic import BaseModel, Field
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str
    isbn: Optional[str] = None
    published_year: Optional[int] = None
    genre: Optional[str] = None
    available: bool = True


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    author: Optional[str] = Field(None, min_length=3, max_length=100)
    isbn: Optional[str] = Field(None, min_length=3, max_length=100)
    published_year: Optional[int] = Field(None, ge=0)
    genre: Optional[str] = Field(None, min_length=3, max_length=50)
    available: Optional[bool] = None


class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True