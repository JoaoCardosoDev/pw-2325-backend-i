FROM python:3.12-alpine

RUN pip install poetry

RUN poetry config virtualenvs.create file

WORKDIR /app

VOLUME ["app"]

COPY . .

RUN poetry install

EXPOSE 8000

CMD python -m api.run
