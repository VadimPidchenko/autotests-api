from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import (
    UpdateCourseRequestSchema,
    UpdateCourseResponseSchema,
    GetCoursesQuerySchema,
    GetCoursesResponseSchema,
    CreateCourseRequestSchema,
    CreateCourseResponseSchema,
)
from fixtures.courses import CoursesFixture
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from tools.allure.epic import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTags
from tools.assertions.base import assert_status_code
from tools.assertions.courses import (
    assert_update_course_response,
    assert_get_courses_response,
    assert_create_course_response,
)
from tools.assertions.schema import validate_json_schema


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTags.AUTHENTICATION, AllureTags.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
class TestCourses:

    @allure.severity(Severity.CRITICAL)
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.sub_suite(AllureStory.UPDATE_ENTITY)
    @allure.tag(AllureTags.UPDATE_ENTITY)
    @allure.title("Update course")
    def test_update_course(
        self, courses_client: CoursesClient, function_create_course: CoursesFixture
    ):
        request = UpdateCourseRequestSchema()
        response = courses_client.update_course_api(
            function_create_course.response.course.id, request
        )
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_course_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.severity(Severity.BLOCKER)
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.sub_suite(AllureStory.GET_ENTITIES)
    @allure.tag(AllureTags.GET_ENTITIES)
    @allure.title("Get courses")
    def test_get_courses(
        self,
        courses_client: CoursesClient,
        function_create_course: CoursesFixture,
        function_create_user: UserFixture,
    ):
        query = GetCoursesQuerySchema(user_id=function_create_user.response.user.id)
        response = courses_client.get_courses_api(query)
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_courses_response(response_data, [function_create_course.response])

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.severity(Severity.BLOCKER)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.tag(AllureTags.CREATE_ENTITY)
    @allure.title("Create course")
    def test_create_course(
        self,
        courses_client: CoursesClient,
        function_create_file: FileFixture,
        function_create_user: UserFixture,
    ):
        request = CreateCourseRequestSchema(
            preview_file_id=function_create_file.response.file.id,
            created_by_user_id=function_create_user.response.user.id,
        )

        response = courses_client.create_course_api(request)
        response_data = CreateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_course_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())
