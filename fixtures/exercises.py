import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import get_exercise_client, ExercisesClient
from clients.exercises.exercises_schema import (
    CreateExercisesRequestSchema,
    CreateExercisesResponseSchema,
)
from fixtures.courses import CoursesFixture
from fixtures.users import UserFixture


class ExerciseFixture(BaseModel):
    request: CreateExercisesRequestSchema
    response: CreateExercisesResponseSchema


@pytest.fixture
def exercises_client(function_create_user: UserFixture) -> ExercisesClient:
    return get_exercise_client(function_create_user.authentication_user)


@pytest.fixture
def function_create_exercise(
    exercises_client: ExercisesClient, function_create_course: CoursesFixture
) -> ExerciseFixture:
    request = CreateExercisesRequestSchema(
        course_id=function_create_course.response.course.id
    )
    response = exercises_client.create_exercise(request)

    return ExerciseFixture(request=request, response=response)
