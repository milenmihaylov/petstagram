FROM python:3

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY manage.py /app/manage.py
COPY static /app/static
COPY static_files /app/static_files
COPY templates /app/templates
COPY media /app/media
COPY petstagram /app/petstagram
