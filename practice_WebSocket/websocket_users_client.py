import asyncio
import websockets

async def client():
    url = 'ws://localhost:8765'
    async with websockets.connect(url) as websocket:
        message = 'Привет, сервер!'
        print(f'Отправка запроса: {message}')
        await websocket.send(message)

        for _ in range(5):
            response = await websocket.recv()
            print(response)


asyncio.run(client())