from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import (
    get_exercise_client,
    CreateExercisesRequestDict,
)
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationCredentialsDict
from clients.users.public_users_client import get_public_users_client, CreateRequestDict
from lesson_HTTPX_CRUD.tools.fakers import get_random_email

public_user_client = get_public_users_client()

create_user_request = CreateRequestDict(
    email=get_random_email(),
    password="string",
    lastName="str",
    firstName="str",
    middleName="str"
)
create_user_response = public_user_client.create_user(create_user_request)


authentication_user = AuthenticationCredentialsDict(
    email=create_user_request["email"],
    password=create_user_request["password"]
)


files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercise_client = get_exercise_client(authentication_user)


create_file_request = CreateFileRequestDict(
    filename="image.png",
    directory="courses",
    upload_file="testdata/files/image.png"
)
create_file_response = files_client.create_file(create_file_request)
print("Create file data:", create_file_response)


create_course_request = CreateCourseRequestDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response["file"]["id"],
    createdByUserId=create_user_response["user"]["id"],
)
create_course_response = courses_client.create_course(create_course_request)
print("Create course data:", create_course_response)


create_exercise_request = CreateExercisesRequestDict(
    title= "Exercise 1",
    courseId= create_course_response["course"]["id"],
    maxScore= 5,
    minScore= 2,
    orderIndex= 1,
    description= "description exercise",
    estimatedTime= "30 minutes"
)
create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print("Create exercise data:", create_exercise_response)