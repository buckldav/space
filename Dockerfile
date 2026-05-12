FROM python:3.14-slim AS base
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1
WORKDIR /app
# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client curl \
    && rm -rf /var/lib/apt/lists/*

# Frontend build stage
FROM node:24-slim AS frontend
WORKDIR /app
COPY package*.json ./
COPY . .
RUN npm i
RUN npm run build

# Production stage
FROM base AS production
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# Copy compiled frontend assets from the frontend stage
COPY --from=frontend /app/space/static /app/space/static
COPY --from=frontend /app/webpack-stats.json /app/webpack-stats.json
RUN python manage.py collectstatic --noinput
EXPOSE 8000
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2"]