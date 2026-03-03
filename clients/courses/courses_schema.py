from pydantic import BaseModel, Field, ConfigDict

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


class CourseSchema(BaseModel):
    """
    Описание структуры курса.
    """
    model_config = ConfigDict(validate_by_name=True)

    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    createdBy_user : UserSchema = Field(alias="createdByUser")

class GetCoursesQuerySchema(BaseModel):
    """
    Определяет структуру query-параметров для получения всех курсов
    пользователя по userId
    """
    model_config = ConfigDict(validate_by_name=True)

    user_id: str = Field(alias="userId")


class CreateCourseRequestSchema(BaseModel):
    """
    Определяет структуру тела запроса на создание курса
    """
    model_config = ConfigDict(validate_by_name=True)

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")


class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    course : CourseSchema

class UpdateCourseRequestSchema(BaseModel):
    """
    Определяет структуру тела запроса на изменение курса
    """
    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")
