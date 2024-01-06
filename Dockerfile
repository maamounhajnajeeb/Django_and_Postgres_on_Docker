FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt && \
    apt-get update && \
    apt-get install -y postgresql-client && \
    apt-get install -y libpq-dev
    # apt-get install -y binutils libproj-dev gdal-bin

COPY . code
WORKDIR /code

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

USER appuser

EXPOSE 8000
