# Приложение на Django Генератора кошелька в Сети Tron 

#### Приложение может:
✅ -генерировать адрес кошелька в сети TRON + seed фразу

✅ -генерировать QR-code для созданного кошелька

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
### 2. Создание файла окружения
создайте файл окружения .env
```
touch .env
```

Отредактируйте .env, указав нужные значения (например, для базы данных):

####  Хост PostgreSQL
POSTGRES_HOST
####  Порт PostgreSQL
POSTGRES_PORT
####  Имя пользователя для подключения
POSTGRES_USER
####  Пароль пользователя
POSTGRES_PASSWORD
####  Название базы данных
POSTGRES_DB


### 3. Сборка и запуск приложения
---
Запустите контейнеры

```
docker-compose up -d --build
```

!!! В проекте лежит файл entrypoint.sh при сборке приложения он автоматически запустит миграции
если по каким то причинам этого не случилось то запустите команду

```
python manage.py migrate 
```
Остановка контейнера

```
docker-compose down
```

### 4. 🛠️ Полезные команды
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
