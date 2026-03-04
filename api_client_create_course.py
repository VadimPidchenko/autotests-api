from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import (
    AuthenticationCredentialsSchema,
)
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.fakers import get_random_email

public_user_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email = get_random_email(),
    password = "string",
    last_name = "Petrovich",
    first_name = "Ivan",
    middle_name = "Sorokin"
)

create_user_response = public_user_client.create_user(create_user_request)

authentication_user =  AuthenticationCredentialsSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

file_client = get_files_client(authentication_user)
course_client = get_courses_client(authentication_user)

create_file_request =  CreateFileRequestSchema(
    filename = "image.png",
    directory= "courses",
    upload_file= "testdata/files/image.png"
)

create_file_response = file_client.create_file(create_file_request)
print("Create file data:", create_file_response)

create_course_request = CreateCourseRequestSchema(
    title = "Python",
    max_score = 100,
    min_score = 10,
    description = "Python API course",
    estimated_time = "2 weeks",
    preview_file_id = create_file_response.file.id,
    created_by_user_id = create_user_response.user.id
)

create_course_response = course_client.create_course(create_course_request)
print("Create course data:", create_course_response)
