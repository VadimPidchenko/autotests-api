import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 5300)
    server_socket.bind(server_address)

    server_socket.listen(5)
    print('Сервер запущен и ждет подключений.....')

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Новое подключение от {client_address}')

        request = client_socket.recv(1024).decode()
        print(f'Получен запрос: {request}')

        response = 'Ответ от сервера, все ОК'
        for i in range(1, 6):
            client_socket.send(f'{i}: {response}'.encode())

        client_socket.close()


if __name__ == '__main__':
    server()
