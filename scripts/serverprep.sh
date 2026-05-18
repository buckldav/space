#!/bin/bash
set -e

DEPLOY_PATH="${1:-.}"

echo "Setting up deployment directory..."
mkdir -p "$DEPLOY_PATH"
cd "$DEPLOY_PATH"

# Create docker-compose.yml for production
cat > docker-compose.yml << 'COMPOSE_EOF'
version: '3.9'

services:
  db:
    image: postgres:15-alpine
    container_name: django_db_prod
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - django_network
    restart: always

  web:
    image: django-app:latest
    container_name: django_web_prod
    command: >
      sh -c "python manage.py migrate &&
             gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 4"
    environment:
      DEBUG: ${DEBUG}
      SECRET_KEY: ${SECRET_KEY}
      ALLOWED_HOSTS: ${ALLOWED_HOSTS}
      DATABASE_URL: postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}
    ports:
      - "8000:8000"
    depends_on:
      - db
    networks:
      - django_network
    restart: always

volumes:
  postgres_data:

networks:
  django_network:
    driver: bridge
COMPOSE_EOF

# Create .env.production template
cat > .env.production.example << 'ENV_EOF'
DEBUG=False
SECRET_KEY=your-production-secret-key-change-this
ALLOWED_HOSTS=your-domain.com,www.your-domain.com

POSTGRES_DB=django_db_prod
POSTGRES_USER=django_user
POSTGRES_PASSWORD=change-this-strong-password
ENV_EOF

echo "Server setup complete!"
echo "Next steps:"
echo "1. Copy .env.production.example to .env.production and update values"
echo "2. Generate a secure SECRET_KEY"
echo "3. Create deploy SSH key: ssh-keygen -t ed25519 -f deploy_key"
echo "4. Add public key to ~/.ssh/authorized_keys on server"
echo "5. Add deploy_key as DEPLOY_KEY secret in GitHub"

