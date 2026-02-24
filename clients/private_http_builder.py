from typing import TypedDict

from httpx import Client

from clients.authentication.authentication_client import (
    get_authentication_client,
    LoginRequestDict,
)

class AuthenticationCredentialsDict(TypedDict):
    """
    Описание структуры запроса на получение авторизованного клиента
    """
    email: str
    password: str

def get_private_http_client(user: AuthenticationCredentialsDict) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationCredentialsDict с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    authentication_client = get_authentication_client()

    login_request = LoginRequestDict(email=user["email"], password=user["password"])
    login_response = authentication_client.login(login_request)

    return Client(
        base_url="http://localhost:8000",
        timeout=10,
        headers={
            "Authorization": f"Bearer {login_response["token"]["accessToken"]}"
        }
    )