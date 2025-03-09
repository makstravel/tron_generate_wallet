#!/bin/sh

# Останавливаем выполнение при ошибке
set -e

echo "Применение миграций..."
python manage.py migrate --noinput

# Запуск сервера
echo "Запуск сервера..."
exec "$@"
