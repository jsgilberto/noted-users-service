# noted-users-service

[![Build Status](https://travis-ci.org/jsgilberto/noted-users-service.svg?branch=master)](https://travis-ci.org/jsgilberto/noted-users-service)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Simple users service for noted app.. Check out the project's [documentation](http://jsgilberto.github.io/noted-users-service/).

## About the project

This repo contains the service for users in noted app. It practically means that it is a service that is being use to manage user registration and authentication through JSON Web Tokens.

## Built with

This project was started with a cookiecutter template from `gh:agconti/cookiecutter-django-rest` which comes with a set of libraries for creating REST APIs with Python and Django:

- Python
- Django
- Django Rest Framework
- Postgres
- Docker
- And more :D

If you want to see the full list please go ahead and read the `requirements.txt` file where you can find all the used dependencies.



## Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)

## Getting started

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Jesus Alvarez - in/alvarezjesus - alv.mtz94@gmail.com

Project link: https://github.com/jsgilberto/noted-users-service