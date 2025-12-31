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
COPY gateway/pyproject.toml gateway/poetry.lock* ./

# Устанавливаем ТОЛЬКО зависимости (без установки самого проекта)
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# Теперь копируем весь код (необязательно, т.к. volume в compose, но на всякий случай)
COPY gateway/proto ./proto
events {}

http {
    include mime.types;
    sendfile on;

    # ===== HTTP → HTTPS (и для Certbot challenge) =====
    server {
        listen 80;
        server_name kload.ru www.kload.ru;

        location /.well-known/acme-challenge/ {
            root /var/www/certbot;
        }

        location / {
            return 301 https://$host$request_uri;
        }
    }

    # ===== HTTPS =====
    server {
        listen 443 ssl;
        server_name kload.ru www.kload.ru;

        ssl_certificate /etc/letsencrypt/live/kload.ru/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/kload.ru/privkey.pem;

        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_prefer_server_ciphers on;
        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
        add_header X-Frame-Options DENY;
        add_header X-Content-Type-Options nosniff;

        # Фронтенд (SPA)
        location / {
            proxy_pass http://frontend:80;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        # API через gateway
        location /api/ {
            proxy_pass http://gateway:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
# PYTHONPATH для proto
ENV PYTHONPATH="${PYTHONPATH}:/app/proto"

# Запуск Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers" , "--forwarded-allow-ips", "*"]