from pydantic import BaseModel, Field, EmailStr, ConfigDict

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

    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


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

    email: EmailStr | None
    last_name: str | None = Field(alias="lastName")
    first_name: str | None = Field(alias="firstName")
    middle_name: str | None = Field(alias="middleName")


class UpdateUserResponseSchema(BaseModel):
    """
    Структура модели ответа для обновления пользователя
    """

    user : UserSchema
