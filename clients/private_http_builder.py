from functools import lru_cache

from httpx import Client
from pydantic import EmailStr, BaseModel, ConfigDict

from clients.authentication.authentication_client import (
    get_authentication_client
)
from clients.authentication.authentication_schema import LoginRequestSchema
from clients.event_hooks import (
    curl_event_hook,
    log_response_event_hook,
    log_request_event_hook,
)
from config import settings


class AuthenticationCredentialsSchema(BaseModel):
    """
    Описание структуры запроса на получение авторизованного клиента
    """
    model_config = ConfigDict(frozen=True)

    email: EmailStr
    password: str

@lru_cache(maxsize=None)
def get_private_http_client(user: AuthenticationCredentialsSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationCredentialsSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    authentication_client = get_authentication_client()

    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authentication_client.login(login_request)

    return Client(
        base_url=settings.http_client.client_url,
        timeout=settings.http_client.timeout,
        headers={
            "Authorization": f"Bearer {login_response.token.access_token}"
        },
        event_hooks={
            "request": [curl_event_hook, log_request_event_hook],
            "response": [log_response_event_hook]
        }
    )
