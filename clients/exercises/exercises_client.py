from httpx import Response

from clients.api_client import APIClient
from clients.exercises.exercises_schema import (
    GetExercisesQuerySchema,
    CreateExercisesRequestSchema,
    CreateExercisesResponseSchema,
    UpdateExercisesRequestSchema,
    GetExerciseResponseSchema,
    GetExercisesResponseSchema,
    UpdateExercisesResponseSchema,
)
from clients.private_http_builder import (
    get_private_http_client,
    AuthenticationCredentialsSchema
)


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод для получения списка заданий для определенного курса.

        :param query: Объект GetExercisesQuerySchema с id курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для получение информации о задании по exercise_id.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises{exercise_id}")

    def create_exercise_api(self, request: CreateExercisesRequestSchema) -> Response:
        """
        Метод для создания задания.

        :param request: Объект CreateExercisesRequestSchema для создания задания с полями: title, courseId,
        maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercise_api(
        self, exercise_id: str, request: UpdateExercisesRequestSchema
    ) -> Response:
        """
        Метод для обновления данных задания.

        :param exercise_id: Идентификатор задания.
        :param request: Объект UpdateExercisesRequestSchema с полями: title, maxScore, minScore,
        orderIndex, description, estimatedTime для обновление задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises{exercise_id}", json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для удаления задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Метод для получение информации о задании по exercise_id.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта GetExerciseResponseSchema.
        """
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Метод для получения списка заданий для определенного курса.

        :param query: Объект GetExercisesQuerySchema с id курса.
        :return: Ответ от сервера в виде объекта GetExercisesResponseSchema.
        """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(
        self, request: CreateExercisesRequestSchema
    ) -> CreateExercisesResponseSchema:
        """
        Метод для создания задания.

        :param request: Объект CreateExercisesRequestSchema для создания задания с полями: title, courseId,
        maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта CreateExercisesResponseSchema
        """
        response = self.create_exercise_api(request)
        return CreateExercisesResponseSchema.model_validate_json(response.text)

    def update_exercise(
        self, exercise_id: str, request: UpdateExercisesRequestSchema
    ) -> UpdateExercisesResponseSchema:
        """
        Метод для обновления данных задания.

        :param exercise_id: Идентификатор задания.
        :param request: Объект UpdateExercisesRequestSchema с полями: title, maxScore, minScore,
        orderIndex, description, estimatedTime для обновление задания.
        :return: Ответ от сервера в виде объекта UpdateExercisesResponseSchema.
        """
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExercisesResponseSchema.model_validate_json(response.text)


def get_exercise_client(user: AuthenticationCredentialsSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :param user: Объект AuthenticationCredentialsSchema с email и password.
    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
