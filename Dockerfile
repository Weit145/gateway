FROM python:3.12-slim

RUN find /etc/apt/sources.list.d/ -type f -name "*.sources" -exec sed -i \
    -e 's|http://deb.debian.org/debian|https://mirror.yandex.ru/debian|g' \
    -e 's|http://security.debian.org/debian-security|https://mirror.yandex.ru/debian-security|g' {} \; && \
    apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry==2.2.1

RUN poetry config virtualenvs.create false

WORKDIR /app

COPY pyproject.toml poetry.lock* ./

# Устанавливаем зависимости (убрал --no-root, чтобы избежать проблем с PEP 621 форматом)
RUN poetry install --no-interaction --no-ansi

COPY . .

ENV PYTHONPATH="${PYTHONPATH}:/app/proto"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]