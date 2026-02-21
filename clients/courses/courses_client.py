from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class GetCoursesQueryDict(TypedDict):
    """
    Определяет структуру query-параметров для получения всех курсов
    пользователя по userId
    """

    userId: str


class CreateCourseRequestDict(TypedDict):
    """
    Определяет структуру тела запроса на создание курса
    """

    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str


class UpdateCourseRequestDict(TypedDict):
    """
    Определяет структуру тела запроса на изменение курса
    """

    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None


class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Метод для получения всех курсов пользователя.

        :param query: id пользователя (userId).
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/courses", params=query)

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод для получения курса по id.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Метод для создания курса.

        :param request: Тело запроса для создание курса с полями: title, maxScore, minScore,
        description, estimatedTime, previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/courses", json=request)

    def update_course_api(
        self, course_id: str, request: UpdateCourseRequestDict
    ) -> Response:
        """
        Метод для обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Тело запроса для обновление курса с полями: title, maxScore, minScore,
        description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод для удаления курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/courses{course_id}")
