import grpc
import course_service_pb2
import course_service_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stab = course_service_pb2_grpc.CourseServiceStub(channel)

response = stab.GetCourse(course_service_pb2.GetCourseRequest(course_id='api-course'))
print(response)

