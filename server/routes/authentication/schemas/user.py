# fastapi
from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    email: EmailStr = Field()
    name: str = Field()
    password: str = Field()
