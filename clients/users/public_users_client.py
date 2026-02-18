from httpx import Response

from clients.api_client import APIClient
from typing import TypedDict


class CreateRequestDict(TypedDict):
    """
    Описание структуры запроса для создания пользователя
    """

    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


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
