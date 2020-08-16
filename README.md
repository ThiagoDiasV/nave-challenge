[![Build Status](https://travis-ci.com/ThiagoDiasV/nave-challenge.svg?branch=master)](https://travis-ci.com/ThiagoDiasV/nave-challenge) [![codecov](https://codecov.io/gh/ThiagoDiasV/nave-challenge/branch/master/graph/badge.svg)](https://codecov.io/gh/ThiagoDiasV/nave-challenge) [![Updates](https://pyup.io/repos/github/ThiagoDiasV/nave-challenge/shield.svg)](https://pyup.io/repos/github/ThiagoDiasV/nave-challenge/) [![Python 3](https://pyup.io/repos/github/ThiagoDiasV/nave-challenge/python-3-shield.svg)](https://pyup.io/repos/github/ThiagoDiasV/nave-challenge/)



# Nave Challenge

## Install and run

Main requirements:

* Python 3.8
* Django 3.1
* Django Rest Framework 3.11
* Django Rest Framework Simple JWT 4.4.0

To ease the experience of using this API, prefer to run inside a Docker container.

### Using Dockerfile and docker-compose

First you need to init a daemon with dockerd, so run dockerd:

    $ sudo dockerd

And then with Docker and docker-compose, run:

    $ docker-compose up --build

This command above will: 
- Create and migrate database 
- Run unit tests
- Run server

Now you will be able to navigate through the Nave API at 0.0.0.0:8000.

By default, the root url will redirect you to `/openapi/swagger/` endpoint. 

### Using local Python 3.8

    Obs: this way has some caveats. To use Postgres as the database management
    system you should create first the database using a local Postgres instance
    and configure the environment variables to communicate correctly with the new
    database. The settings.py file is configured by default to create a SQLite3
    file if you can't or if you wan't to create a Postgres database. 

    If you want to run locally with Postgres as DBMS, rename the .env-docker
    file in nave folder to .env and change the environment variables in .env
    file to allow the correct communication with Postgres. 

Prefer to create a Python virtual environment and then

    (venv) $  pip install -r requirements.txt

After installing requirements run:

    (venv) $ python manage.py migrate
    (venv) $ python manage.py runserver

The API will be available at localhost:8000

By default, the root url will redirect you to `openapi/swagger/` endpoint. 

## Run tests

You can cover Nave API with unit tests running:

### Using Docker

    $ docker-compose exec web pytest

### Using Python 3.8

    (venv) $ pytest

# Rest API

The Rest API is described below

## Endpoints

    /api/signup/
    /api/login/
    /api/token/refresh/
    /api/navers/
    /api/navers/{id}/
    /api/projects/
    /api/projects/{id}/

### How to use API

First of all, you need to register a new user. With the user credentials you need to get a JSON web token to get access to the API features.

#### Signup

Signup a new user on system

* URL

    /api/signup/

* Method

    `POST`

- URL Params

    None

- Data Params

    Required:
    `email=[string]`
    `password=[string]`

- Success Response

    - HTTP status code
        `201 CREATED`

    - Content
        Registered user
        ```
        {
            "id": 2,
            "email": "teste@teste.com"
        }
        ```


#### Get JWT Token
     
Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of those credentials.

* URL

    /api/login/

* Method

    `POST`

- URL Params

    None

- Data Params

    Required:
    `email=[string]`
    `password=[string]`

- Success Response

    - HTTP status code
        `200 OK`

    - Content
        `access` and `refresh` tokens to allow access to the API.
        I.e.
        ```
        {
            "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU5NzYyMzQxMCwianRpIjoiNDg2OTBlNDU0MTZmNDEwNzg1NGM2ODY5N2M1NzI5NjYiLCJ1c2VyX2lkIjoyfQ.T2f8SMnp1qmpVXOi3-jPbt5lVlsGZVf12XsDsG4xzsE",
            "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk3NTM3MzEwLCJqdGkiOiI3N2ZjOTM0ZGQ1Y2I0ZjIzOTllMmU3YzhjYThmNTFiYyIsInVzZXJfaWQiOjJ9.Z62KDEV7gq0E7TsXHnOF6k3X52ffP_3YuFh-MMg6syc"
        }
        ```

#### Refresh JWT Token

Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.

* URL

    /api/token/refresh/

* Method

    `POST`

- URL Params

    None

- Data Params

    Required:
    `refresh=[string]`

- Success Response

    - HTTP status code
        `200 OK`

    - Content
        `access` token.
        I.e.
        ```
        {
            "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk3NTM3NTIzLCJqdGkiOiJiYTA4OTU5MmZiMmM0NzExYTAyZDk2MmFkMzFhNTgwMiIsInVzZXJfaWQiOjJ9.qGmWlLceDGtcRF_icfKj5FiDH_6W3pd4aQyjerIADsU"
        }
        ```

#### Navers and Projects endpoints

Take a look at `/openapi/swagger/` endpoint to see how to send HTTP requests to Nave API. 

You must send the `access token` in a `Authorization: Bearer` string with each header of a HTTP request. 

If you are using Postman, open label `Headers`, the `key` must be `Authorization` and the `value` should be the `access token` received.


## API documentation endpoints

In these endpoints it's possible to user two UI's to interate with Nave API

    /openapi/swagger/
    /openapi/redoc/
