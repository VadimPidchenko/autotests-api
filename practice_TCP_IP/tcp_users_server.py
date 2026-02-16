import socket

def server():
    user_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    user_server_address = ('localhost', 12345)
    user_server_socket.bind(user_server_address)

    user_server_socket.listen(10)
    print('Сервер запущен и ждет подключений..... ')

    message_list = []

    while True:
        client_socket, client_address = user_server_socket.accept()
        print(f'Пользователь с адресом: {client_address} подключился к серверу')

        request = client_socket.recv(1024).decode()
        print(f'Пользователь с адресом: {client_address} отправил сообщение: {request}')

        message_list.append(request)
        client_socket.send('\n'.join(message_list).encode())

        client_socket.close()


if __name__ == '__main__':
    server()