from pydantic import BaseModel, Field, EmailStr, ConfigDict

from tools.fakers import fake


class UserSchema(BaseModel):
    """
    Описание модели пользователя.
    """

    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class GetUserResponseSchema(BaseModel):
    """
    Описание модели ответа на получение пользователя.
    """

    user: UserSchema


class CreateUserRequestSchema(BaseModel):
    """
    Описание модели запроса для создания пользователя
    """
    model_config = ConfigDict(validate_by_name=True)

    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str = Field(alias="middleName", default_factory=fake.middle_name)


class CreateUserResponseSchema(BaseModel):
    """
    Описание модели ответа на запрос для создания пользователя
    """

    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    """
    Структура модели для обновления пользователя
    """
    model_config = ConfigDict(validate_by_name=True)

    email: EmailStr | None = Field(default_factory=fake.email)
    last_name: str | None = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str | None = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str | None = Field(alias="middleName", default_factory=fake.middle_name)


class UpdateUserResponseSchema(BaseModel):
    """
    Структура модели ответа для обновления пользователя
    """

    user : UserSchema
