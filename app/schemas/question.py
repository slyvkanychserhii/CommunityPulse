from pydantic import BaseModel, Field


class QuestionCreate(BaseModel):
    text: str = Field(..., min_length=12)
    category_id: int


class QuestionResponse(BaseModel):
    id: int
    text: str
    category_id: int

    class Config:
        # Указываем Pydantic использовать эти параметры чтобы можно было переносить данные прямо с объекта
        from_attributes = True
