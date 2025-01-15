#!/bin/bash


echo "Waiting for the database to be ready..."


until alembic upgrade head; do
  echo "Waiting for database to be available for migrations..."
  sleep 1
done


exec uvicorn main:app --host 0.0.0.0 --port 8000
