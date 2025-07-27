from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    year: str
    score: int
