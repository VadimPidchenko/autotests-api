import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 5300)
client_socket.connect(server_address)

message = 'Запрос от клиента, Привет !'
client_socket.send(message.encode())

response = client_socket.recv(1024).decode()
print(f'Получен ответ от сервера: {response} ')

client_socket.close()