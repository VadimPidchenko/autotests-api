import grpc

import user_service_pb2
import user_service_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stab = user_service_pb2_grpc.UserServiceStub(channel)

response = stab.GetUser(user_service_pb2.GetUserRequest(username ='Вадим'))
print(response)

