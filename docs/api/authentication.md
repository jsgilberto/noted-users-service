# Authentication
For clients to authenticate, the token key should be included in the Authorization HTTP header. The key should be prefixed by the string literal "Bearer", with whitespace separating the two strings. For example:

```
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

Unauthenticated responses that are denied permission will result in an HTTP `401 Unauthorized` response with an appropriate `WWW-Authenticate` header. For example:

```
WWW-Authenticate: Bearer
```

The curl command line tool may be useful for testing JWT authenticated APIs. For example, assuming /api/v1/example/ is a protected resource which requires authentication:

```bash
curl -X GET http://127.0.0.1:8000/api/v1/example/ -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAzNDAxMTg2LCJqdGkiOiI4M2IzN2JkOTg2MDM0MWM3YTVjMzZjMjA4MTRiZTI5YiIsInVzZXJfaWQiOiJhNjQ4NGMyZS01MjQ4LTQxYmEtODE0Yi0yNWY2NzE0MjMxY2IifQ.UumlsITnfcMGylT2UPsoS-wv3oZ2xxvWZSuCwQJzz7w'
```

## Retrieving JWT
Authorization JSON Web Tokens are issued and returned when a registered user asks for a token using the following API endpoint:

**Request**:

`POST` `/api/token/`

**Request body**

```json
{
    "email": "email@domain.com",
    "password": "your_password"
}
```


**Response**:
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYwMzUwMDA1MiwianRpIjoiNWU0MjJkMDcwOWM0NGU2ODkyNzJkZWEwYzYwN2I3YzYiLCJ1c2VyX2lkIjoiOTdjNzY3ODEtODQwNi00ZGNhLWE2ZjktZTJlNDIzOGNmMTE3In0.fH0oAHgYBLhZXhxkOmsBYQqd3SfYb6NtT2iR9tU7tdA",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAzNDEzOTUyLCJqdGkiOiIwZmRmMmQ4MTZmM2E0ZWY4ODA2MmVjN2NiZWYxMWQ4MyIsInVzZXJfaWQiOiI5N2M3Njc4MS04NDA2LTRkY2EtYTZmOS1lMmU0MjM4Y2YxMTcifQ.Lj_1KgNTjrly_O4le4GeT1JtRwEshHZ4fyNn_2krGHY"
}
```

## Refreshing JWT

When this short-lived access token expires, you can use the longer-lived refresh token to obtain another access token:
```bash
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4"}' \
  http://localhost:8000/api/token/refresh/
```

## Verifying JWT
You can also verify if a token is valid making a call to the following endpoint:

**Request**:

`POST` `/api/token/verify/`

**Request body**

```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```