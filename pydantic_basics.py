from pydantic import BaseModel, Field, ConfigDict, HttpUrl, EmailStr, ValidationError
from pydantic.alias_generators import to_camel
import uuid

class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    #Так же мы можем добавлять методы в схему для представления данных
    #Метод не должен делать api запросов и содержать бизнес логику
    #Он нужен только для удобного представления данных из схемы
    def get_user_full_name(self) -> str:
        return f"{self.first_name}{self.last_name}"


class CourseSchema(BaseModel):
    #Создали конфиг для всей схемы в целом
    #Определили, что можем передавать данные в модель как по алиасу, так и по названию поля, определенного в схеме
    model_config = ConfigDict(validate_by_name=True)

    id: str = Field(default_factory=lambda : str(uuid.uuid4()))
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=100)
    min_score: int = Field(alias="minScore", default=10)
    description: str = "Playwright"
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default="1 week")
    created_by_user : UserSchema = Field(alias="createdByUser")


# Первый сопоб инициализации модели через объект
course_default_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    preview_file=FileSchema(
        id="file-id",
        url="http://localhost:8000",
        filename="file.png",
        directory="courses",
    ),
    estimatedTime="1 week",
    createdByUser=UserSchema(
        id="user-id",
        email="user@gmail.com",
        lastName="Bond",
        firstName="Zara",
        middleName="Alise",
    ),
)

print("Инициализация модели через объект")
print("Course default model:", course_default_model)

# Второй способ инициализации модели через словарь
# Определяем словарь с данными
course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "id": "file-id",
        "filename": "file.png",
        "url": "http://localhost:8000",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alise"
    }
}

# Используем распаковку при инициализации объекта
course_dict_model = CourseSchema(**course_dict)
print("Инициализация модели через словарь")
print("Course dict model:", course_dict_model)

# Третий способ инициализации модели через строку JSON
# Определяем JSON с данными
course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alise"
    }
}
"""

course_json_model = CourseSchema.model_validate_json(course_json)
print("Инициализация модели через строку JSON")
print("Course JSON model:", course_json_model)


# Сериализация из объекта модели в словарь, строку JSON
print("Сериализация из объекта модели в словарь в snake_case")
print(course_json_model.model_dump())
print("Сериализация из объекта модели в строку JSON в snake_case")
print(course_json_model.model_dump_json())

# Если мы хотим сериализовать модель в camelCase
print("Сериализация из объекта модели в словарь в camelCase")
print(course_json_model.model_dump(by_alias=True))
print("Сериализация из объекта модели в строку JSON в camelCase")
print(course_json_model.model_dump_json(by_alias=True))

# # Создание "пустого" объекта модели с значениями по умолчанию
# default_course = CourseSchema()
# print("Default course schema:", default_course)
#
# # Создание "пустого" объекта модели с значениями по умолчанию с использованием default_factory
# default_course1 = CourseSchema()
# default_course2 = CourseSchema()
# print("Default course schema 1:", default_course1)
# print("Default course schema 2:", default_course2)

#Инициализируем объект FileSchema с некорректным url
#Оорачиваем его в try/except
print("Инициализируем объект FileSchema с некорректным url")
try:
    file = FileSchema(
        id="file-id",
        url="localhost",
        filename="file.png",
        directory="courses",
    )
except ValidationError as error:
    print(error)
    print(error.errors())


