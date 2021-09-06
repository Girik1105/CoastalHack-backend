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

# Users
```
users/register/
```
Methods allowed: GET
Parameters needed: None

This endpoint returns a list of all users.

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

# Communities
```
/api/communities/create/
```
Methods allowed: POST
Parameters needed: 
{
"Authorization":"JWT {{ access token }},
"name":"",
"description":"",
"cover":"",
}

Use this endpoint to create communities

```
/api/communities/list/
```
Methods allowed: GET
Parameters needed: 
{
"Authorization":"JWT {{ access token }},
}
or no parameters (no auth is needed for listing communities)

use this endpoint to list all communities 

```
/api/communities/edit/<community slug>
```
Methods allowed: PATCH
Parameters needed: 
{
"Authorization":"JWT {{ access token }},
"name":"",
"description":"",
"cover":"",
}

use this endpoint to edit a community, only the owner can send a patch request (it will raise unauthorized error if someone else tries to access it)
Partial data is allowed at this endpoint

```
/api/communities/delete/<community slug>
```
Methods allowed: DELETE
Parameters needed: 
{
"Authorization":"JWT {{ access token }},
}

use this endpoint to delete a community, only the owner can delete (it will raise unauthorized error if someone else tries to access it)


# Tests
```
python manage.py test
```