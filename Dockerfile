# Используем официальный образ Python
FROM python:3.11

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Создаем рабочую директорию
WORKDIR /tron_app

# Копируем зависимости и устанавливаем их
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Обновляем pip
RUN pip install --upgrade pip

# Копируем все файлы проекта
COPY . .

# Указываем настройки Django
ENV DJANGO_SETTINGS_MODULE=config.settings

# Копируем entrypoint.sh и делаем его исполняемым
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Указываем entrypoint
ENTRYPOINT ["/entrypoint.sh"]
