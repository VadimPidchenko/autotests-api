from httpx import Response

from clients.api_client import APIClient
from typing import TypedDict

from clients.public_http_builder import get_public_http_client


class User(TypedDict):
    """
    Описание структуры пользователя
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


class CreateRequestDict(TypedDict):
    """
    Описание структуры запроса для создания пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class CreateResponseDict(TypedDict):
    """
    Описание структуры ответа на запрос для создания пользователя
    """
    user: User

class PublicUsersClient(APIClient):
    """
    Публичный API (не требующий авторизации) для создания клиента
    """

    def create_user_api(self, request: CreateRequestDict) -> Response:
        """
        Метод для создания нового пользователя

        :param request: Словарь с данными для создания пользователя (email, password, lastName, firstName, middleName)
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)

    def create_user(self, request: CreateRequestDict) -> CreateResponseDict:
        """
        Метод для создания нового пользователя

        :param request: Словарь с данными для создания пользователя (email, password, lastName, firstName, middleName)
        :return: Распарсенный ответ от сервера в виде словаря
        """
        response = self.create_user_api(request)
        return response.json()


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())
