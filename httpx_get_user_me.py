import httpx

login_payload = {
    "email": "vadim123.user@example.com",
    "password": "12345"
}

login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()

print('Login status code:', login_response.status_code)
print('Login data:', login_response_data)

get_user_me_headers = {
    'Authorization': f'Bearer {login_response_data['token']['accessToken']}'
}

get_user_me_response = httpx.get('http://localhost:8000/api/v1/users/me', headers=get_user_me_headers)
get_user_me_response_data = get_user_me_response.json()

print('Get user status code:', get_user_me_response.status_code)
print('User data:', get_user_me_response_data)