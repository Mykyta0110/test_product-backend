#!/bin/bash


echo "Waiting for the database to be ready..."
until nc -z -v -w30 db_products 5432; do
  echo "Waiting for db_products to be available..."
  sleep 1
done


echo "Running Alembic migrations..."
alembic upgrade head


exec uvicorn main:app --host 0.0.0.0 --port 8000
