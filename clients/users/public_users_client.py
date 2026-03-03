from httpx import Response

from clients.api_client import APIClient

from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class PublicUsersClient(APIClient):
    """
    Публичный API (не требующий авторизации) для создания клиента
    """

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Метод для создания нового пользователя

        :param request: Объект CreateUserRequestSchema с данными для создания пользователя (email, password, lastName, firstName, middleName)
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        """
        Метод для создания нового пользователя

        :param request: Объект CreateUserRequestSchema с данными для создания пользователя (email, password, lastName, firstName, middleName)
        :return: Ответ от сервера в виде объекта CreateUserResponseSchema
        """
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())
