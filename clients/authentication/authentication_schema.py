from pydantic import BaseModel, Field

class TokenSchema(BaseModel):
    """
    Описание структуры аутентификационных токенов.
    """
    tokenType: str = Field(alias="tokenType")
    accessToken: str = Field(alias="accessToken")
    refreshToken: str = Field(alias="refreshToken")

class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str

class LoginResponseSchema(BaseModel):
    """
    Описание структуры ответа аутентификации.
    """
    token : TokenSchema

class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления токена.
    """
    refreshToken: str = Field(alias="refreshToken")
