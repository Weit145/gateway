FROM python:3.12-slim

RUN find /etc/apt/sources.list.d/ -type f -name "*.sources" -exec sed -i \
    -e 's|http://deb.debian.org/debian|https://mirror.yandex.ru/debian|g' \
    -e 's|http://security.debian.org/debian-security|https://mirror.yandex.ru/debian-security|g' {} \; && \
    apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*



# Poetry

RUN pip install --no-cache-dir poetry==2.2.1



WORKDIR /app



# Копируем зависимости

COPY gateway/pyproject.toml gateway/poetry.lock* ./

RUN poetry config virtualenvs.create false && poetry install --no-root



# Копируем код приложения **в корень /app**

COPY gateway/app ./app



# Копируем proto из auth-service


COPY auth-service/proto ./proto


COPY gateway/proto ./proto




ENV PYTHONPATH="${PYTHONPATH}:/app/proto"

# Запуск FastAPI

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
