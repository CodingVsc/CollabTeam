# CollabTeam

##Проект предназачен для коллаборации разработчиков в разработке различных продуктов. НАХОДИТСЯ НА ДОРАБОТКЕ. Модели написаны, но не запушены. 
## Старт

```
git clone https://gitlab.com/DJWOMS/collabteam.git

Переименовать .env.example на .env

docker-compose up --build

Не выключая контейнеры выполнить команду

docker exec -it collab_team-net-back alembic upgrade head
```

## Создание миграций
1) В `migrations/base.py` импортировать модуль с моделями.

2) Выполнить команду создания файла миграций.
```
alembic revision --autogenerate -m 'название модели или миграции'
```
3) Проверить созданный файл миграций. Alembic не умеет работать с переименованием таблиц и полей.

4) Выполнить миграцию (изменения в бд)
```
alembic upgrade head
```

## Запуск проекта
1) Запускаем проект коммандой:
```
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000 --log-level debug --use-colors
```
2) Переходим по ссылке: http://127.0.0.1:8000/docs

## Folders

- core - директория для общих настроек
- core/db.py - настройки базы данных
- core/settings.py - настройки для проекта
- core/db/session.py - настройки сессии БД
- core/share - базовые классы для controllers, models, services и т.д.
- media - media файлы: картинки, pdf и т.д.
- static - static файлы: css, js и т.д.
- migrations - директория alembic для миграций
- migrations/versions - файлы миграций
- migrations/base.py - файл с импортированными модулями моделей для работы автогенерации миграций
- migrations/env.py - скрипт alembic для работы миграций
- src - верхний уровень приложения, содержит общие маршруты, main.py, все сервисы (приложения)
- src/main.py - корень проекта, который запускает приложение FastAPI
- src/routers.py - общие routers для всех приложений проекта

## Files
Каждый пакет (приложение) имеет свои router, schemas, models и т.д.

- repository.py - repository
- controllers.py - ядро каждого модуля со всеми endpoints
- service.py - специфичная для модуля бизнес-логика
- models.py - для моделей БД
- schemas.py - для pydantic моделей
- routers.py - общие routers для всех контроллеров модуля
- dependencies.py - зависимости для приложения
- utils.py - функции, не относящиеся к бизнес-логике
- exceptions.py - специфические для модуля исключения
- constants.py - константы

## Running console commands:
To run console commands use next syntax (in root directory): core/cmds.py <command> [options]

List of available commands:

## Схема БД проекта:

https://drive.google.com/file/d/17o79C5bMGoplcsoetIjcqPVbG0D5FJ-T/view?usp=sharing


## Используемы инструменты

- python - 3.11
- fastapi - 0.100.0
- sqlalchemy - 2.0.18
- postgres - 15.3
- docker compose - 3.9
