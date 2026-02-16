import httpx

login_payload = {
    "email": "vadim123.user@example.com",
    "password": "12345"
}

login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()

print("Status code:", login_response.status_code)
print("Login data:", login_response_data)

refresh_payload = {
    'refreshToken': login_response_data['token']['refreshToken']
}

refresh_response = httpx.post('http://localhost:8000/api/v1/authentication/refresh', json=refresh_payload)
refresh_response_data = refresh_response.json()

print('Refresh status code', refresh_response.status_code)
print('Refresh response:', refresh_response_data)