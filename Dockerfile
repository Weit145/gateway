# Используем Python на базе Debian Bookworm (стабильнее для РФ)
FROM python:3.12-slim

# Системные зависимости с российским зеркалом
RUN find /etc/apt/sources.list.d/ -type f -name "*.sources" -exec sed -i \
    -e 's|http://deb.debian.org/debian|https://mirror.yandex.ru/debian|g' \
    -e 's|http://security.debian.org/debian-security|https://mirror.yandex.ru/debian-security|g' {} \; && \
    apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry==2.2.1

# Зеркало PyPI Яндекса для скорости
ENV POETRY_PYPI_MIRROR_URL=https://mirror.yandex.ru/mirrors/pypi/simple/

# Рабочая директория
WORKDIR /app

# Копируем только файлы зависимостей для кэширования
COPY pyproject.toml poetry.lock* ./

# Отключаем виртуальное окружение и устанавливаем зависимости (включая сам проект)
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Теперь копируем весь код
COPY . .

# Добавляем proto в PYTHONPATH (если нужно для импортов)
ENV PYTHONPATH="${PYTHONPATH}:/app/proto"

# Запускаем через uvicorn (как в compose)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]