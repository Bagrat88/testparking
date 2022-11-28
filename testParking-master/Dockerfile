FROM python:3.11.0-alpine

RUN pip install --upgrade pip setuptools wheel poetry

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]