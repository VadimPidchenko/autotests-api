from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.authentication.authentication_client import (
    AuthenticationClient,
)
from clients.authentication.authentication_schema import (
    LoginRequestSchema,
    LoginResponseSchema,
)
from fixtures.users import UserFixture
from tools.allure.epic import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTags
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.authentication
@pytest.mark.regression
@allure.tag(AllureTags.AUTHENTICATION, AllureTags.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
class TestAuthentication:

    @allure.severity(Severity.BLOCKER)
    @allure.story(AllureStory.LOGIN)
    @allure.title("Login with correct email and password")
    def test_login(
        self,
        function_create_user: UserFixture,
        authentication_client: AuthenticationClient,
    ):
        request = LoginRequestSchema(
            email=function_create_user.email, password=function_create_user.password
        )
        response = authentication_client.login_api(request)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        # проверка результата
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_response(response_data)

        # валидация JSON schema
        validate_json_schema(response.json(), response_data.model_json_schema())
