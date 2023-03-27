FROM python:3.11-slim

ENV PYTHONBUFFERED 1

ADD /src /src
ADD pyproject.toml /src

WORKDIR /src

RUN pip3 --upgrade pip & pip3 install poetry

RUN poetry install
