from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import (
    get_private_http_client,
    AuthenticationCredentialsDict,
)


class Exercise(TypedDict):
    """
    Определяет структуру задания
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExerciseResponseDict(TypedDict):
    """
    Определяет структуру тела ответа на получение задания
    """
    exercise: Exercise


class GetExercisesResponseDict(TypedDict):
    """
    Определяет структуру тела ответа на получение списка заданий
    """
    exercises: list[Exercise]


class GetExercisesQueryDict(TypedDict):
    """
    Определяет структуру query-параметров для получения списка заданий
    для определенного курса (courseId)
    """
    courseId: str

class CreateExercisesRequestDict(TypedDict):
    """
    Определяет структуру тела запроса на создание задания
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class CreateExercisesResponseDict(TypedDict):
    """
    Определяет структуру тела ответа на создание задания
    """
    exercise: Exercise


class UpdateExercisesRequestDict(TypedDict):
    """
    Определяет структуру тела запроса на изменение задания
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class UpdateExercisesResponseDict(TypedDict):
    """
    Определяет структуру тела ответа на изменение задания
    """
    exercise: Exercise


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод для получения списка заданий для определенного курса.

        :param query: id курса (courseId).
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для получение информации о задании по exercise_id.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises{exercise_id}")

    def create_exercise_api(self, request: CreateExercisesRequestDict) -> Response:
        """
        Метод для создания задания.

        :param request: Тело запроса для создания задания с полями: title, courseId, maxScore, minScore,
        orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(
        self, exercise_id: str, request: UpdateExercisesRequestDict
    ) -> Response:
        """
        Метод для обновления данных задания.

        :param exercise_id: Идентификатор задания.
        :param request: Тело запроса для обновление задания с полями: title, maxScore, minScore,
        orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для удаления задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Метод для получение информации о задании по exercise_id.

        :param exercise_id: Идентификатор задания.
        :return: Распарсенный ответ от сервера в виде словаря структуры : GetExerciseResponseDict
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Метод для получения списка заданий для определенного курса.

        :param query: id курса (courseId).
        :return: Распарсенный ответ от сервера в виде словаря структуры : GetExercisesResponseDict
        """
        response = self.get_exercises_api(query)
        return response.json()

    def create_exercise(
        self, request: CreateExercisesRequestDict
    ) -> CreateExercisesResponseDict:
        """
        Метод для создания задания.

        :param request: Тело запроса для создания задания с полями: title, courseId, maxScore, minScore,
        orderIndex, description, estimatedTime.
        :return: Распарсенный ответ от сервера в виде словаря структуры : CreateExercisesResponseDict
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(
        self, exercise_id: str, request: UpdateExercisesRequestDict
    ) -> UpdateExercisesResponseDict:
        """
        Метод для обновления данных задания.

        :param exercise_id: Идентификатор задания.
        :param request: Тело запроса для обновление задания с полями: title, maxScore, minScore,
        orderIndex, description, estimatedTime.
        :return: Распарсенный ответ от сервера в виде словаря структуры : UpdateExercisesResponseDict
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


def get_exercise_client(user: AuthenticationCredentialsDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :param user: email и пароль
    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
