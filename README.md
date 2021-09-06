# CoastalHack-backend

REST API with Django Rest Framework 

# SETUP AND INSTALLATION 

Download requirements:
```
pip install -r requirements.txt
```
Then run the python file:
```
python manage.py runserver 
```

# Endpoints:

# Auth Endpoints 
```
users/register/
```
To Create Users 
Methods allowed: POST
Parameters needed: 
{
"email":"",
"user_name"",
"Password":""
}

```
api/token/
```
To get JWT access and refresh Token
Methods allowed: POST
Parameters needed: 
{
"email":"",
"Password":""
}

The access and refresh token need to be stored within the frontend. The access token expires in % minutes after it is issued. The refresh token, however, expires in a day.

```
api/token/refresh/
```
Refresh Token

```
/api/auth/jwt/refresh/
```
To refresh JWT tokens 
Methods allowed: POST
Parameters needed: 
{
"refresh"
}

To get a new access and refresh token, send a post request to this endpoint to get a new access and refresh token 

Logout

```
/users/logout/blacklist/
```
To blacklist access JWT tokens once a user logouts so they don't use the same token to get refresh tokens
Methods allowed: POST
Parameters needed: 
{
"refresh"
}

# Tests

```
python manage.py test
