import socket

user_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

user_server_address = ('localhost', 12345)
user_client_socket.connect(user_server_address)

message = 'Привет, сервер!'
user_client_socket.send(message.encode())

print(user_client_socket.recv(1024).decode())

user_client_socket.close()