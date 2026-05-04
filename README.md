version: '3.9'

services:
web:
build:
context: .
dockerfile: docker/django/Dockerfile

    container_name: django_app
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - ./backend:/app
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - db

db:
image: postgres:15
environment:
POSTGRES_DB: ${POSTGRES_DB}
POSTGRES_USER: ${POSTGRES_USER}
POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
ports:

- "5432:5432"