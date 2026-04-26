import curlify2
from httpx import Request, RequestNotRead

"""
curl -X 'POST' \
  'http://localhost:8000/api/v1/users' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "user@example.com",
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}'
"""


def make_curl_from_request(request: Request) -> str:

    """
    Генерирует команду cURL из HTTP-запроса httpx.

    :param request: HTTP-запрос, из которого будет сформирована команда cURL.
    :return: Строка с командой cURL, содержащая метод запроса, URL, заголовки и тело (если есть).
    """

    result : list[str] = [f"curl -X '{request.method}'", f"'{request.url}'"]

    for header, valure in request.headers.items():
        result.append(f"-H '{header}: {valure}'")

    try:
        if body := request.content:
            result.append(f"-d '{body.decode("utf-8")}'")
    except RequestNotRead:
        pass

    return "\\\n".join(result)
