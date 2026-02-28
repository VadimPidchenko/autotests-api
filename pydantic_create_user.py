from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    """Схема описывающая пользователя (основные данные)."""
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """Схема запроса на создание пользователя."""
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """Схема ответа при создании пользователя (содержит объект пользователя)."""
    user: UserSchema
