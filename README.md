# Приложение на Django Генератора кошелька в Сети Tron в Docker с SQLite

Этот проект содержит Django-приложение, упакованное в Docker, с использованием базы данных SQLite.

## ⚙️ Установка и запуск

### 1. Клонирование репозитория
Копировать репозиторий
```
git clone https://github.com/makstravel/tron_generate_wallet.git
```
перейти в папку с репозиторием
```
cd tron_generate_wallet
```

В проекте лежит файл entrypoint.sh при сборке приложения он автоматически запустит миграции

если по каким то причинам этого не случилось то запустите команду
```
python manage.py migrate 
```

Запустите контейнеры

```
docker-compose up -d --build
```

Остановка контейнера

```
docker-compose down
```

🛠️ Полезные команды
Пересобрать контейнер	docker-compose up -d --build
Просмотреть логи контейнера	docker logs -f django_app
Запустить команду внутри контейнера	docker exec -it django_app sh
Создать суперпользователя Django	docker exec -it django_app python manage.py createsuperuser

```sh
Структура проекта

├── Django_tron/          # Исходный код Django  приложения
├── Dockerfile            # Инструкция сборки Docker-образа
├── docker-compose.yml    # Конфигурация Docker Compose
├── entrypoint.sh         # Скрипт запуска Django (миграции + runserver)
└── requirements.txt      # Зависимости проекта
