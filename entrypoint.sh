#!/bin/bash

# Очікуємо, поки база даних стане доступною (якщо потрібно, але Render дасть вам правильний URL)
echo "Waiting for the database to be ready..."

# Якщо ви використовуєте Alembic для міграцій, перевірте, чи підключається до правильного URL
until alembic upgrade head; do
  echo "Waiting for database to be available for migrations..."
  sleep 1
done

# Запускаємо FastAPI додаток
exec uvicorn main:app --host 0.0.0.0 --port 8000
