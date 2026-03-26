import pytest
from pydantic import BaseModel

from clients.authentication.authentication_client import (
    get_authentication_client,
    AuthenticationClient,
)
from clients.private_http_builder import AuthenticationCredentialsSchema
from clients.users.private_users_client import (
    get_private_users_client,
    PrivateUsersClient,
)
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self):
        return self.request.email

    @property
    def password(self):
        return self.request.password

    @property
    def authentication_user(self):
        return AuthenticationCredentialsSchema(email=self.email, password=self.password)


@pytest.fixture
def public_user_client() -> PublicUsersClient:
    return get_public_users_client()


@pytest.fixture
def authentication_client() -> AuthenticationClient:
    return get_authentication_client()


@pytest.fixture
def function_create_user(public_user_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_user_client.create_user(request)

    return UserFixture(request=request, response=response)


@pytest.fixture
def private_user_client(function_create_user) -> PrivateUsersClient:
    return get_private_users_client(function_create_user.authentication_user)
