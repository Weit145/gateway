# Базовый образ
FROM python:3.12-slim

# Российские зеркала для apt
RUN find /etc/apt/sources.list.d/ -type f -name "*.sources" -exec sed -i \
    -e 's|http://deb.debian.org/debian|https://mirror.yandex.ru/debian|g' \
    -e 's|http://security.debian.org/debian-security|https://mirror.yandex.ru/debian-security|g' {} \; && \
    apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry==2.2.1

# Зеркало PyPI Яндекса
ENV POETRY_PYPI_MIRROR_URL=https://mirror.yandex.ru/mirrors/pypi/simple/

# Отключаем виртуальное окружение
RUN poetry config virtualenvs.create false

# Рабочая директория
WORKDIR /app

# Копируем файлы зависимостей
COPY pyproject.toml poetry.lock* ./

# Устанавливаем ТОЛЬКО зависимости (без установки самого проекта)
RUN poetry install --no-root --only main --no-interaction --no-ansi

# Теперь копируем весь код (необязательно, т.к. volume в compose, но на всякий случай)
COPY . .

# PYTHONPATH для proto
ENV PYTHONPATH="${PYTHONPATH}:/app/proto"

# Запуск Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]