FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ../.. .

EXPOSE 8000

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && gunicorn recipes_backend.wsgi:application --bind 0.0.0.0:8000"]
