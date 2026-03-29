import pytest
from pydantic import BaseModel

from clients.courses.courses_client import get_courses_client, CoursesClient
from clients.courses.courses_schema import (
    CreateCourseRequestSchema,
    CreateCourseResponseSchema,
)
from fixtures.files import FileFixture
from fixtures.users import UserFixture


class CoursesFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema

@pytest.fixture
def courses_client(function_create_user: UserFixture) -> CoursesClient:
    return get_courses_client(function_create_user.authentication_user)


@pytest.fixture
def function_create_course(
    courses_client: CoursesClient,
    function_create_file: FileFixture,
    function_create_user: UserFixture,
) -> CoursesFixture:
    request = CreateCourseRequestSchema(
        preview_file_id=function_create_file.response.file.id,
        created_by_user_id=function_create_user.response.user.id,
    )

    response = courses_client.create_course(request)

    return CoursesFixture(request=request, response=response)
