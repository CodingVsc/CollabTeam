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

- createsuperuser[Uploading Копия БД CollabTeam.drawio.xml…]()<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" modified="2024-02-23T12:20:21.709Z" agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36" etag="RC0xdcKxjqdilRhZX-QG" version="23.0.2" type="google">
  <diagram name="Page-1" id="2ca16b54-16f6-2749-3443-fa8db7711227">
    <mxGraphModel dx="3872" dy="4116" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1100" pageHeight="850" background="none" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="Nov7NwWhawipYWJH2YjQ-2" value="User" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#00CC00;" parent="1" vertex="1">
          <mxGeometry x="-363" y="-1000" width="180" height="390" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-3" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-2" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-4" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-3" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-5" value="id (UUID)" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-3" vertex="1">
          <mxGeometry x="70" width="110" height="30" as="geometry">
            <mxRectangle width="110" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-12" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-2" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-13" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-12" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-14" value="username" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-12" vertex="1">
          <mxGeometry x="70" width="110" height="30" as="geometry">
            <mxRectangle width="110" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-15" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-2" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-16" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-15" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-17" value="password" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-15" vertex="1">
          <mxGeometry x="70" width="110" height="30" as="geometry">
            <mxRectangle width="110" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-18" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-2" vertex="1">
          <mxGeometry y="120" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-19" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-18" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-20" value="first_name" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-18" vertex="1">
          <mxGeometry x="70" width="110" height="30" as="geometry">
            <mxRectangle width="110" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-21" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-2" vertex="1">
          <mxGeometry y="150" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-22" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-21" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-23" value="last_name" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-21" vertex="1">
          <mxGeometry x="70" width="110" height="30" as="geometry">
            <mxRectangle width="110" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-24" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-2" vertex="1">
          <mxGeometry y="180" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-25" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-24" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-26" value="email" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-24" vertex="1">
          <mxGeometry x="70" width="110" height="30" as="geometry">
            <mxRectangle width="110" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-27" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-2" vertex="1">
          <mxGeometry y="210" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-28" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-27" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-29" value="avatar" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-27" vertex="1">
          <mxGeometry x="70" width="110" height="30" as="geometry">
            <mxRectangle width="110" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-30" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-2" vertex="1">
          <mxGeometry y="240" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-31" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-30" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-32" value="is_banned" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-30" vertex="1">
          <mxGeometry x="70" width="110" height="30" as="geometry">
            <mxRectangle width="110" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-33" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-2" vertex="1">
          <mxGeometry y="270" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-34" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-33" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-35" value="is_active" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-33" vertex="1">
          <mxGeometry x="70" width="110" height="30" as="geometry">
            <mxRectangle width="110" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-36" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-2" vertex="1">
          <mxGeometry y="300" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-37" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-36" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-38" value="is_superuser" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-36" vertex="1">
          <mxGeometry x="70" width="110" height="30" as="geometry">
            <mxRectangle width="110" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-39" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-2" vertex="1">
          <mxGeometry y="330" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-40" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-39" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-41" value="created_at" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-39" vertex="1">
          <mxGeometry x="70" width="110" height="30" as="geometry">
            <mxRectangle width="110" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-42" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-2" vertex="1">
          <mxGeometry y="360" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-43" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-42" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-44" value="update_at" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-42" vertex="1">
          <mxGeometry x="70" width="110" height="30" as="geometry">
            <mxRectangle width="110" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-45" value="Personal Info" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#00CC00;" parent="1" vertex="1">
          <mxGeometry x="-750" y="-990" width="180" height="240" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-46" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-45" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-47" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-46" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-48" value="id " style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-46" vertex="1">
          <mxGeometry x="70" width="110" height="30" as="geometry">
            <mxRectangle width="110" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-58" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-45" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-59" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-58" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-60" value="site" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-58" vertex="1">
          <mxGeometry x="70" width="110" height="30" as="geometry">
            <mxRectangle width="110" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-61" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-45" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-62" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-61" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-63" value="about(CV descrp)" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-61" vertex="1">
          <mxGeometry x="70" width="110" height="30" as="geometry">
            <mxRectangle width="110" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-64" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-45" vertex="1">
          <mxGeometry y="120" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-65" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-64" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-66" value="time_zone" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-64" vertex="1">
          <mxGeometry x="70" width="110" height="30" as="geometry">
            <mxRectangle width="110" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-67" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-45" vertex="1">
          <mxGeometry y="150" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-68" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-67" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-69" value="dev_exp" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-67" vertex="1">
          <mxGeometry x="70" width="110" height="30" as="geometry">
            <mxRectangle width="110" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-87" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-45" vertex="1">
          <mxGeometry y="180" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-88" value="&lt;b&gt;FK&lt;/b&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-87" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-89" value="&lt;b&gt;&lt;u&gt;USER UUID&lt;/u&gt;&lt;/b&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-87" vertex="1">
          <mxGeometry x="70" width="110" height="30" as="geometry">
            <mxRectangle width="110" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-32" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-45" vertex="1">
          <mxGeometry y="210" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-33" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="so0dwTSsRMgNjVHivWw8-32" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-34" value="language" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="so0dwTSsRMgNjVHivWw8-32" vertex="1">
          <mxGeometry x="70" width="110" height="30" as="geometry">
            <mxRectangle width="110" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-124" value="&lt;b&gt;&lt;u&gt;Social_Accounts&lt;/u&gt;&lt;/b&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#00CC00;" parent="1" vertex="1">
          <mxGeometry x="-680" y="-600" width="180" height="150" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-125" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-124" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-126" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-125" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-127" value="id " style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-125" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-128" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-124" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-129" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-128" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-130" value="name" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-128" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-131" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-124" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-132" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-131" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-133" value="metadata" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-131" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-83" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-124" vertex="1">
          <mxGeometry y="120" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-84" value="&lt;b&gt;FK&lt;/b&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-83" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-85" value="&lt;b&gt;&lt;u&gt;USER&amp;nbsp;UUID&lt;br&gt;&lt;/u&gt;&lt;/b&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-83" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-148" value="&lt;u&gt;Permission&lt;br&gt;&lt;/u&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;" parent="1" vertex="1">
          <mxGeometry x="-130" y="-490" width="180" height="120" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-149" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-148" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-150" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-149" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-151" value="id " style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-149" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-152" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-148" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-153" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-152" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-154" value="name" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-152" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-155" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-148" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-156" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-155" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-157" value="codename" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-155" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-158" value="&lt;u&gt;UserPermission&lt;/u&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;" parent="1" vertex="1">
          <mxGeometry x="-363" y="-490" width="180" height="120" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-159" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-158" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-160" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-159" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-161" value="id " style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-159" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-162" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-158" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-163" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-162" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-164" value="permissions" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-162" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-165" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-158" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-166" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-165" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-167" value="user UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-165" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-239" value="SoicalNetwork" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#00CC00;" parent="1" vertex="1">
          <mxGeometry x="-1020" y="-880" width="180" height="130" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-240" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-239" vertex="1">
          <mxGeometry y="30" width="180" height="40" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-241" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-240" vertex="1">
          <mxGeometry width="40" height="40" as="geometry">
            <mxRectangle width="40" height="40" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-242" value="id " style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-240" vertex="1">
          <mxGeometry x="40" width="140" height="40" as="geometry">
            <mxRectangle width="140" height="40" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-243" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-239" vertex="1">
          <mxGeometry y="70" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-244" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-243" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-245" value="name" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-243" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-246" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-239" vertex="1">
          <mxGeometry y="100" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-247" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-246" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-248" value="icon" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-246" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-250" value="UserSocial" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#00CC00;" parent="1" vertex="1">
          <mxGeometry x="-990" y="-1160" width="180" height="160" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-251" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-250" vertex="1">
          <mxGeometry y="30" width="180" height="40" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-252" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-251" vertex="1">
          <mxGeometry width="40" height="40" as="geometry">
            <mxRectangle width="40" height="40" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-253" value="id " style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-251" vertex="1">
          <mxGeometry x="40" width="140" height="40" as="geometry">
            <mxRectangle width="140" height="40" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-254" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-250" vertex="1">
          <mxGeometry y="70" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-255" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-254" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-256" value="user_id" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-254" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-257" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-250" vertex="1">
          <mxGeometry y="100" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-258" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-257" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-259" value="social_network_id" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-257" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-260" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-250" vertex="1">
          <mxGeometry y="130" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-261" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-260" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-262" value="link" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-260" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="YDDpKSoIlpt64208BBWw-26" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" parent="1" source="LJFPJaAqwbhQFGvEF_o8-50" target="qAa2Pi7rPlZP1lqOzIKF-38" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-349" value="&lt;b&gt;Team&lt;/b&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#007FFF;" parent="1" vertex="1">
          <mxGeometry x="-20" y="-1550" width="180" height="210" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-350" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-349" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-351" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-350" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Nov7NwWhawipYWJH2YjQ-352" value="UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="Nov7NwWhawipYWJH2YjQ-350" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-2" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-349" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-3" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="so0dwTSsRMgNjVHivWw8-2" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-4" value="language" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="so0dwTSsRMgNjVHivWw8-2" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-42" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-349" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-43" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="so0dwTSsRMgNjVHivWw8-42" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-44" value="name" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="so0dwTSsRMgNjVHivWw8-42" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-45" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-349" vertex="1">
          <mxGeometry y="120" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-46" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="so0dwTSsRMgNjVHivWw8-45" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-47" value="about" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="so0dwTSsRMgNjVHivWw8-45" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-2" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-349" vertex="1">
          <mxGeometry y="150" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-3" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-2" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-4" value="Owner UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-2" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ukp7RBHOysZNrc7Xjoi0-1" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="Nov7NwWhawipYWJH2YjQ-349" vertex="1">
          <mxGeometry y="180" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="ukp7RBHOysZNrc7Xjoi0-2" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="ukp7RBHOysZNrc7Xjoi0-1" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ukp7RBHOysZNrc7Xjoi0-3" value="logo" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="ukp7RBHOysZNrc7Xjoi0-1" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-1" value="Project" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#FF6666;" parent="1" vertex="1">
          <mxGeometry x="220" y="-1020" width="193" height="330" as="geometry" />
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-2" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LU-fPexgcIpwWTkRIjDJ-1" vertex="1">
          <mxGeometry y="30" width="193" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-3" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-2" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-4" value="id (UUID)" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-2" vertex="1">
          <mxGeometry x="70" width="123" height="30" as="geometry">
            <mxRectangle width="123" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-5" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LU-fPexgcIpwWTkRIjDJ-1" vertex="1">
          <mxGeometry y="60" width="193" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-6" value="&lt;b&gt;FK&lt;/b&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-5" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-7" value="&lt;b&gt;&lt;u&gt;GithubRepo&lt;/u&gt;&lt;/b&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-5" vertex="1">
          <mxGeometry x="70" width="123" height="30" as="geometry">
            <mxRectangle width="123" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-8" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LU-fPexgcIpwWTkRIjDJ-1" vertex="1">
          <mxGeometry y="90" width="193" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-9" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-8" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-10" value="name" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-8" vertex="1">
          <mxGeometry x="70" width="123" height="30" as="geometry">
            <mxRectangle width="123" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-11" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LU-fPexgcIpwWTkRIjDJ-1" vertex="1">
          <mxGeometry y="120" width="193" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-12" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-11" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-13" value="describe" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-11" vertex="1">
          <mxGeometry x="70" width="123" height="30" as="geometry">
            <mxRectangle width="123" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-14" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LU-fPexgcIpwWTkRIjDJ-1" vertex="1">
          <mxGeometry y="150" width="193" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-15" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-14" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-16" value="category" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-14" vertex="1">
          <mxGeometry x="70" width="123" height="30" as="geometry">
            <mxRectangle width="123" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-17" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LU-fPexgcIpwWTkRIjDJ-1" vertex="1">
          <mxGeometry y="180" width="193" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-18" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-17" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-19" value="tools" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-17" vertex="1">
          <mxGeometry x="70" width="123" height="30" as="geometry">
            <mxRectangle width="123" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-20" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LU-fPexgcIpwWTkRIjDJ-1" vertex="1">
          <mxGeometry y="210" width="193" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-21" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-20" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-22" value="project_owner UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-20" vertex="1">
          <mxGeometry x="70" width="123" height="30" as="geometry">
            <mxRectangle width="123" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-64" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LU-fPexgcIpwWTkRIjDJ-1" vertex="1">
          <mxGeometry y="240" width="193" height="30" as="geometry" />
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-65" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="bdqJI-T08oNJTsnCjI4d-64" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-66" value="is_banned" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="bdqJI-T08oNJTsnCjI4d-64" vertex="1">
          <mxGeometry x="70" width="123" height="30" as="geometry">
            <mxRectangle width="123" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-29" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LU-fPexgcIpwWTkRIjDJ-1" vertex="1">
          <mxGeometry y="270" width="193" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-30" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-29" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-31" value="is_active" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-29" vertex="1">
          <mxGeometry x="70" width="123" height="30" as="geometry">
            <mxRectangle width="123" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-32" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LU-fPexgcIpwWTkRIjDJ-1" vertex="1">
          <mxGeometry y="300" width="193" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-33" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-32" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-34" value="created_at" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-32" vertex="1">
          <mxGeometry x="70" width="123" height="30" as="geometry">
            <mxRectangle width="123" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-38" value="&lt;b&gt;&lt;u&gt;Github Repository&lt;/u&gt;&lt;/b&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#FF6666;" parent="1" vertex="1">
          <mxGeometry x="-130" y="-940" width="180" height="240" as="geometry" />
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-39" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LU-fPexgcIpwWTkRIjDJ-38" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-40" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-39" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-41" value="id " style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-39" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-42" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LU-fPexgcIpwWTkRIjDJ-38" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-43" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-42" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-44" value="name" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-42" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-45" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LU-fPexgcIpwWTkRIjDJ-38" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-46" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-45" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-47" value="url" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-45" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-48" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LU-fPexgcIpwWTkRIjDJ-38" vertex="1">
          <mxGeometry y="120" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-49" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-48" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-50" value="stars" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-48" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-51" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LU-fPexgcIpwWTkRIjDJ-38" vertex="1">
          <mxGeometry y="150" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-52" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-51" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-53" value="commits_value" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-51" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-54" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LU-fPexgcIpwWTkRIjDJ-38" vertex="1">
          <mxGeometry y="180" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-55" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-54" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-56" value="forks_value" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-54" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-57" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LU-fPexgcIpwWTkRIjDJ-38" vertex="1">
          <mxGeometry y="210" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-58" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-57" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-59" value="last_commit_date" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LU-fPexgcIpwWTkRIjDJ-57" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-61" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="1" vertex="1">
          <mxGeometry x="20" y="-1120" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-64" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="1" vertex="1">
          <mxGeometry x="20" y="-1090" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-77" value="Только гитхаб" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;" parent="1" vertex="1">
          <mxGeometry x="-710" y="-680" width="100" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-86" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#79FF40;" parent="1" source="LU-fPexgcIpwWTkRIjDJ-83" target="Nov7NwWhawipYWJH2YjQ-3" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="-490" y="-465" />
              <mxPoint x="-490" y="-495" />
              <mxPoint x="-471" y="-495" />
              <mxPoint x="-471" y="-900" />
              <mxPoint x="-410" y="-900" />
              <mxPoint x="-410" y="-920" />
              <mxPoint x="-380" y="-920" />
              <mxPoint x="-380" y="-940" />
              <mxPoint x="-363" y="-940" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-90" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#FF00FF;" parent="1" source="LU-fPexgcIpwWTkRIjDJ-87" target="Nov7NwWhawipYWJH2YjQ-3" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="-520" y="-795" />
              <mxPoint x="-520" y="-955" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="LU-fPexgcIpwWTkRIjDJ-91" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="Nov7NwWhawipYWJH2YjQ-257" target="Nov7NwWhawipYWJH2YjQ-240" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="-1010" y="-1045" />
              <mxPoint x="-1010" y="-980" />
              <mxPoint x="-820" y="-980" />
              <mxPoint x="-820" y="-830" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-12" value="&lt;u&gt;CategoryGroup&lt;br&gt;&lt;/u&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#FF6666;" parent="1" vertex="1">
          <mxGeometry x="530" y="-930" width="180" height="120" as="geometry" />
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-13" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="so0dwTSsRMgNjVHivWw8-12" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-14" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="so0dwTSsRMgNjVHivWw8-13" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-15" value="id " style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="so0dwTSsRMgNjVHivWw8-13" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-16" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="so0dwTSsRMgNjVHivWw8-12" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-17" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="so0dwTSsRMgNjVHivWw8-16" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-18" value="catrgory uuid" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="so0dwTSsRMgNjVHivWw8-16" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-32" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="so0dwTSsRMgNjVHivWw8-12" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-33" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-32" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-34" value="project UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-32" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-22" value="&lt;u&gt;ToolsGroup&lt;br&gt;&lt;/u&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#FF6666;" parent="1" vertex="1">
          <mxGeometry x="530" y="-790" width="180" height="120" as="geometry" />
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-23" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="so0dwTSsRMgNjVHivWw8-22" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-24" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="so0dwTSsRMgNjVHivWw8-23" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-25" value="id " style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="so0dwTSsRMgNjVHivWw8-23" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-26" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="so0dwTSsRMgNjVHivWw8-22" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-27" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="so0dwTSsRMgNjVHivWw8-26" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-28" value="tools uuid" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="so0dwTSsRMgNjVHivWw8-26" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-28" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="so0dwTSsRMgNjVHivWw8-22" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-29" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-28" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-30" value="project UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-28" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-1" value="&lt;u&gt;Board&lt;/u&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#FFB570;" parent="1" vertex="1">
          <mxGeometry x="350" y="-580" width="180" height="150" as="geometry" />
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-2" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="qAa2Pi7rPlZP1lqOzIKF-1" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-3" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="qAa2Pi7rPlZP1lqOzIKF-2" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-4" value="UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="qAa2Pi7rPlZP1lqOzIKF-2" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-5" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="qAa2Pi7rPlZP1lqOzIKF-1" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-6" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="qAa2Pi7rPlZP1lqOzIKF-5" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-7" value="title" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="qAa2Pi7rPlZP1lqOzIKF-5" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-8" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="qAa2Pi7rPlZP1lqOzIKF-1" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-9" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="qAa2Pi7rPlZP1lqOzIKF-8" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-10" value="Owner UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="qAa2Pi7rPlZP1lqOzIKF-8" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-18" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="qAa2Pi7rPlZP1lqOzIKF-1" vertex="1">
          <mxGeometry y="120" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-19" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-18" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-20" value="created_at" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-18" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-35" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="Nov7NwWhawipYWJH2YjQ-162" target="Nov7NwWhawipYWJH2YjQ-149" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-41" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="LU-fPexgcIpwWTkRIjDJ-5" target="LU-fPexgcIpwWTkRIjDJ-39" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="so0dwTSsRMgNjVHivWw8-60" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="1" vertex="1">
          <mxGeometry x="-20" y="-1050" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-11" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#72FF2B;" parent="1" source="qAa2Pi7rPlZP1lqOzIKF-8" target="Nov7NwWhawipYWJH2YjQ-39" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-20" value="&lt;u&gt;Column&lt;/u&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#FFB570;" parent="1" vertex="1">
          <mxGeometry x="570" y="-580" width="180" height="150" as="geometry" />
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-21" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="qAa2Pi7rPlZP1lqOzIKF-20" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-22" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="qAa2Pi7rPlZP1lqOzIKF-21" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-23" value="UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="qAa2Pi7rPlZP1lqOzIKF-21" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-24" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="qAa2Pi7rPlZP1lqOzIKF-20" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-25" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="qAa2Pi7rPlZP1lqOzIKF-24" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-26" value="title" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="qAa2Pi7rPlZP1lqOzIKF-24" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-27" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="qAa2Pi7rPlZP1lqOzIKF-20" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-28" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="qAa2Pi7rPlZP1lqOzIKF-27" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-29" value="position" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="qAa2Pi7rPlZP1lqOzIKF-27" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-42" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="qAa2Pi7rPlZP1lqOzIKF-20" vertex="1">
          <mxGeometry y="120" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-43" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-42" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-44" value="Board UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-42" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-37" value="&lt;u&gt;Card&lt;/u&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#FFB570;" parent="1" vertex="1">
          <mxGeometry x="470" y="-360" width="180" height="300" as="geometry" />
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-38" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="qAa2Pi7rPlZP1lqOzIKF-37" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-39" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="qAa2Pi7rPlZP1lqOzIKF-38" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-40" value="UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="qAa2Pi7rPlZP1lqOzIKF-38" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-41" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="qAa2Pi7rPlZP1lqOzIKF-37" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-42" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="qAa2Pi7rPlZP1lqOzIKF-41" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-43" value="title" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="qAa2Pi7rPlZP1lqOzIKF-41" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-44" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="qAa2Pi7rPlZP1lqOzIKF-37" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-45" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="qAa2Pi7rPlZP1lqOzIKF-44" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-46" value="description" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="qAa2Pi7rPlZP1lqOzIKF-44" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-47" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="qAa2Pi7rPlZP1lqOzIKF-37" vertex="1">
          <mxGeometry y="120" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-48" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="qAa2Pi7rPlZP1lqOzIKF-47" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-49" value="includes" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="qAa2Pi7rPlZP1lqOzIKF-47" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-50" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="qAa2Pi7rPlZP1lqOzIKF-37" vertex="1">
          <mxGeometry y="150" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-51" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="qAa2Pi7rPlZP1lqOzIKF-50" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-52" value="position" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="qAa2Pi7rPlZP1lqOzIKF-50" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-57" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="qAa2Pi7rPlZP1lqOzIKF-37" vertex="1">
          <mxGeometry y="180" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-58" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="qAa2Pi7rPlZP1lqOzIKF-57" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-59" value="Card Creater UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="qAa2Pi7rPlZP1lqOzIKF-57" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-46" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="qAa2Pi7rPlZP1lqOzIKF-37" vertex="1">
          <mxGeometry y="210" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-47" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-46" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-48" value="Column UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-46" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-50" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="qAa2Pi7rPlZP1lqOzIKF-37" vertex="1">
          <mxGeometry y="240" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-51" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-50" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-52" value="created_at" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-50" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-53" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="qAa2Pi7rPlZP1lqOzIKF-37" vertex="1">
          <mxGeometry y="270" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-54" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-53" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-55" value="deadline_date" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-53" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="qAa2Pi7rPlZP1lqOzIKF-65" value="Trello Clone" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;" parent="1" vertex="1">
          <mxGeometry x="505" y="-642" width="90" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="Nov7NwWhawipYWJH2YjQ-254" target="Nov7NwWhawipYWJH2YjQ-3" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="-530" y="-1075" />
              <mxPoint x="-530" y="-955" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-3" value="&lt;b&gt;TeamMembers&lt;/b&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#FF99FF;" parent="1" vertex="1">
          <mxGeometry x="-670" y="-1510" width="180" height="180" as="geometry" />
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-4" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LJFPJaAqwbhQFGvEF_o8-3" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-5" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-4" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-6" value="id " style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-4" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-10" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LJFPJaAqwbhQFGvEF_o8-3" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-11" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-10" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-12" value="&lt;b style=&quot;border-color: var(--border-color);&quot;&gt;&lt;u style=&quot;border-color: var(--border-color);&quot;&gt;Team UUID&lt;/u&gt;&lt;/b&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-10" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-13" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LJFPJaAqwbhQFGvEF_o8-3" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-14" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-13" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-15" value="User UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-13" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-8" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LJFPJaAqwbhQFGvEF_o8-3" vertex="1">
          <mxGeometry y="120" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-9" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-8" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-10" value="is_lead" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-8" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="cOokgg_9ec5KLx6cwFXG-4" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LJFPJaAqwbhQFGvEF_o8-3" vertex="1">
          <mxGeometry y="150" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="cOokgg_9ec5KLx6cwFXG-5" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="cOokgg_9ec5KLx6cwFXG-4" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="cOokgg_9ec5KLx6cwFXG-6" value="position ID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="cOokgg_9ec5KLx6cwFXG-4" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-31" value="&lt;u&gt;LinkGroup&lt;br&gt;&lt;/u&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#007FFF;" parent="1" vertex="1">
          <mxGeometry x="260" y="-1520" width="180" height="120" as="geometry" />
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-32" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LJFPJaAqwbhQFGvEF_o8-31" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-33" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-32" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-34" value="id " style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-32" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-35" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LJFPJaAqwbhQFGvEF_o8-31" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-36" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-35" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-37" value="link" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-35" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-39" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LJFPJaAqwbhQFGvEF_o8-31" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-40" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-39" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-41" value="team UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-39" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-45" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="LJFPJaAqwbhQFGvEF_o8-42" target="qAa2Pi7rPlZP1lqOzIKF-2" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-49" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="LJFPJaAqwbhQFGvEF_o8-46" target="qAa2Pi7rPlZP1lqOzIKF-21" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-56" value="&lt;u&gt;Label&lt;/u&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#FFB570;" parent="1" vertex="1">
          <mxGeometry x="1110" y="-290" width="180" height="150" as="geometry" />
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-57" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LJFPJaAqwbhQFGvEF_o8-56" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-58" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-57" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-59" value="UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-57" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-60" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LJFPJaAqwbhQFGvEF_o8-56" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-61" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-60" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-62" value="name" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-60" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-35" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LJFPJaAqwbhQFGvEF_o8-56" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-36" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="E6rGj8i0a1SSwwkenldq-35" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-37" value="color" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="E6rGj8i0a1SSwwkenldq-35" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-48" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LJFPJaAqwbhQFGvEF_o8-56" vertex="1">
          <mxGeometry y="120" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-49" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="E6rGj8i0a1SSwwkenldq-48" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-50" value="Board UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="E6rGj8i0a1SSwwkenldq-48" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-72" value="&lt;u&gt;CardMembers&lt;br&gt;&lt;/u&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#FF99FF;" parent="1" vertex="1">
          <mxGeometry x="110" y="-220" width="180" height="120" as="geometry" />
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-73" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LJFPJaAqwbhQFGvEF_o8-72" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-74" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-73" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-75" value="UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-73" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-76" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LJFPJaAqwbhQFGvEF_o8-72" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-77" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-76" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="LJFPJaAqwbhQFGvEF_o8-78" value="USER UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="LJFPJaAqwbhQFGvEF_o8-76" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-1" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="LJFPJaAqwbhQFGvEF_o8-72" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-2" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-1" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-3" value="card uuid" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-1" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-7" value="&lt;u&gt;BoardMembers&lt;br&gt;&lt;/u&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#FF99FF;" parent="1" vertex="1">
          <mxGeometry x="120" y="-380" width="180" height="120" as="geometry" />
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-8" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="AwyTIWYlYU0fc9ncyoPG-7" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-9" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-8" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-10" value="UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-8" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-11" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="AwyTIWYlYU0fc9ncyoPG-7" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-12" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-11" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-13" value="USER UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-11" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-14" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="AwyTIWYlYU0fc9ncyoPG-7" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-15" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-14" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-16" value="Board uuid" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-14" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-21" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="AwyTIWYlYU0fc9ncyoPG-14" target="qAa2Pi7rPlZP1lqOzIKF-2" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-22" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#B266FF;" parent="1" source="AwyTIWYlYU0fc9ncyoPG-11" target="Nov7NwWhawipYWJH2YjQ-3" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="-170" y="-305" />
              <mxPoint x="-170" y="-955" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-23" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#009999;" parent="1" source="qAa2Pi7rPlZP1lqOzIKF-57" target="Nov7NwWhawipYWJH2YjQ-3" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="460" y="-165" />
              <mxPoint x="460" y="-240" />
              <mxPoint x="110" y="-240" />
              <mxPoint x="110" y="-960" />
              <mxPoint x="-183" y="-960" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-24" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#FF8578;" parent="1" source="LJFPJaAqwbhQFGvEF_o8-13" target="Nov7NwWhawipYWJH2YjQ-3" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-25" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="LJFPJaAqwbhQFGvEF_o8-10" target="Nov7NwWhawipYWJH2YjQ-350" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-26" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="LJFPJaAqwbhQFGvEF_o8-39" target="Nov7NwWhawipYWJH2YjQ-350" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="215" y="-1415" />
              <mxPoint x="215" y="-1490" />
              <mxPoint x="160" y="-1490" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-27" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#FF9933;" parent="1" source="LU-fPexgcIpwWTkRIjDJ-20" target="Nov7NwWhawipYWJH2YjQ-3" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="150" y="-795" />
              <mxPoint x="150" y="-990" />
              <mxPoint x="-160" y="-990" />
              <mxPoint x="-160" y="-955" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-31" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="AwyTIWYlYU0fc9ncyoPG-28" target="LU-fPexgcIpwWTkRIjDJ-2" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="471" y="-685" />
              <mxPoint x="471" y="-980" />
              <mxPoint x="413" y="-980" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-35" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1.016;entryY=0.849;entryDx=0;entryDy=0;entryPerimeter=0;" parent="1" source="AwyTIWYlYU0fc9ncyoPG-32" target="LU-fPexgcIpwWTkRIjDJ-2" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="500" y="-825" />
              <mxPoint x="500" y="-965" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-36" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="Nov7NwWhawipYWJH2YjQ-165" target="Nov7NwWhawipYWJH2YjQ-15" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-37" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="LJFPJaAqwbhQFGvEF_o8-76" target="Nov7NwWhawipYWJH2YjQ-21" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="-430" y="-145" />
              <mxPoint x="-430" y="-835" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-38" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="AwyTIWYlYU0fc9ncyoPG-1" target="qAa2Pi7rPlZP1lqOzIKF-38" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-40" value="&lt;u&gt;Request&lt;br&gt;&lt;/u&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#FF99FF;" parent="1" vertex="1">
          <mxGeometry x="-400" y="-1325" width="180" height="240" as="geometry" />
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-41" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="AwyTIWYlYU0fc9ncyoPG-40" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-42" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-41" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-43" value="UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-41" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-44" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="AwyTIWYlYU0fc9ncyoPG-40" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-45" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-44" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-46" value="user UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-44" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-47" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="AwyTIWYlYU0fc9ncyoPG-40" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-48" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-47" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-49" value="team UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-47" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-60" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="AwyTIWYlYU0fc9ncyoPG-40" vertex="1">
          <mxGeometry y="120" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-61" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-60" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-62" value="message" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-60" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-14" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="AwyTIWYlYU0fc9ncyoPG-40" vertex="1">
          <mxGeometry y="150" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-15" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="E6rGj8i0a1SSwwkenldq-14" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-16" value="is_accept" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="E6rGj8i0a1SSwwkenldq-14" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-20" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="AwyTIWYlYU0fc9ncyoPG-40" vertex="1">
          <mxGeometry y="180" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-21" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="E6rGj8i0a1SSwwkenldq-20" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-22" value="is_rejected" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="E6rGj8i0a1SSwwkenldq-20" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-20" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="AwyTIWYlYU0fc9ncyoPG-40" vertex="1">
          <mxGeometry y="210" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-21" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-20" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-22" value="created_at" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-20" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-50" value="&lt;u&gt;Invite&lt;br&gt;&lt;/u&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#FF99FF;" parent="1" vertex="1">
          <mxGeometry x="-120" y="-1325" width="180" height="240" as="geometry" />
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-51" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="AwyTIWYlYU0fc9ncyoPG-50" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-52" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-51" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-53" value="UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-51" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-54" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="AwyTIWYlYU0fc9ncyoPG-50" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-55" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-54" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-56" value="user UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-54" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-57" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="AwyTIWYlYU0fc9ncyoPG-50" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-58" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-57" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-59" value="team UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-57" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-66" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="AwyTIWYlYU0fc9ncyoPG-50" vertex="1">
          <mxGeometry y="120" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-67" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-66" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-68" value="message" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="AwyTIWYlYU0fc9ncyoPG-66" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-17" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="AwyTIWYlYU0fc9ncyoPG-50" vertex="1">
          <mxGeometry y="150" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-18" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="E6rGj8i0a1SSwwkenldq-17" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-19" value="is_accept" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="E6rGj8i0a1SSwwkenldq-17" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-23" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="AwyTIWYlYU0fc9ncyoPG-50" vertex="1">
          <mxGeometry y="180" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-24" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="E6rGj8i0a1SSwwkenldq-23" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-25" value="is_rejected" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="E6rGj8i0a1SSwwkenldq-23" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-17" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="AwyTIWYlYU0fc9ncyoPG-50" vertex="1">
          <mxGeometry y="210" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-18" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-17" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-19" value="created_at" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-17" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-69" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#30FF45;" parent="1" source="AwyTIWYlYU0fc9ncyoPG-47" target="Nov7NwWhawipYWJH2YjQ-350" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="-180" y="-1205" />
              <mxPoint x="-180" y="-1500" />
              <mxPoint x="-20" y="-1500" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-70" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=-0.022;entryY=0.241;entryDx=0;entryDy=0;entryPerimeter=0;" parent="1" source="AwyTIWYlYU0fc9ncyoPG-57" target="Nov7NwWhawipYWJH2YjQ-350" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="-160" y="-1205" />
              <mxPoint x="-160" y="-1355" />
              <mxPoint x="-40" y="-1355" />
              <mxPoint x="-40" y="-1513" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-71" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.001;entryY=0.261;entryDx=0;entryDy=0;entryPerimeter=0;strokeColor=#FF0080;" parent="1" source="AwyTIWYlYU0fc9ncyoPG-44" target="Nov7NwWhawipYWJH2YjQ-3" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="-200" y="-1250" />
              <mxPoint x="-200" y="-1070" />
              <mxPoint x="-383" y="-1070" />
              <mxPoint x="-383" y="-962" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="AwyTIWYlYU0fc9ncyoPG-74" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.995;entryY=0.104;entryDx=0;entryDy=0;entryPerimeter=0;" parent="1" source="AwyTIWYlYU0fc9ncyoPG-54" target="Nov7NwWhawipYWJH2YjQ-3" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="62q4ZuEUndfMt-47XOB3-1" value="&lt;u&gt;Category&lt;br&gt;&lt;/u&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#FF6666;" parent="1" vertex="1">
          <mxGeometry x="770" y="-930" width="180" height="90" as="geometry" />
        </mxCell>
        <mxCell id="62q4ZuEUndfMt-47XOB3-2" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="62q4ZuEUndfMt-47XOB3-1" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="62q4ZuEUndfMt-47XOB3-3" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="62q4ZuEUndfMt-47XOB3-2" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="62q4ZuEUndfMt-47XOB3-4" value="id " style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="62q4ZuEUndfMt-47XOB3-2" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="62q4ZuEUndfMt-47XOB3-5" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="62q4ZuEUndfMt-47XOB3-1" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="62q4ZuEUndfMt-47XOB3-6" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="62q4ZuEUndfMt-47XOB3-5" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="62q4ZuEUndfMt-47XOB3-7" value="name" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="62q4ZuEUndfMt-47XOB3-5" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="62q4ZuEUndfMt-47XOB3-29" value="&lt;u&gt;Tool&lt;br&gt;&lt;/u&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#FF6666;" parent="1" vertex="1">
          <mxGeometry x="770" y="-790" width="180" height="90" as="geometry" />
        </mxCell>
        <mxCell id="62q4ZuEUndfMt-47XOB3-30" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="62q4ZuEUndfMt-47XOB3-29" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="62q4ZuEUndfMt-47XOB3-31" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="62q4ZuEUndfMt-47XOB3-30" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="62q4ZuEUndfMt-47XOB3-32" value="id " style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="62q4ZuEUndfMt-47XOB3-30" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="62q4ZuEUndfMt-47XOB3-33" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="62q4ZuEUndfMt-47XOB3-29" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="62q4ZuEUndfMt-47XOB3-34" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="62q4ZuEUndfMt-47XOB3-33" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="62q4ZuEUndfMt-47XOB3-35" value="name" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="62q4ZuEUndfMt-47XOB3-33" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=-0.02;entryY=0.192;entryDx=0;entryDy=0;entryPerimeter=0;" parent="1" source="so0dwTSsRMgNjVHivWw8-26" target="62q4ZuEUndfMt-47XOB3-30" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="so0dwTSsRMgNjVHivWw8-16" target="62q4ZuEUndfMt-47XOB3-2" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-51" value="&lt;u&gt;CardsLabel&lt;/u&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#FFB570;" parent="1" vertex="1">
          <mxGeometry x="840" y="-290" width="180" height="120" as="geometry" />
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-52" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="E6rGj8i0a1SSwwkenldq-51" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-53" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="E6rGj8i0a1SSwwkenldq-52" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-54" value="UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="E6rGj8i0a1SSwwkenldq-52" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-55" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="E6rGj8i0a1SSwwkenldq-51" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-56" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="E6rGj8i0a1SSwwkenldq-55" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-57" value="Card UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="E6rGj8i0a1SSwwkenldq-55" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-58" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="E6rGj8i0a1SSwwkenldq-51" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-59" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="E6rGj8i0a1SSwwkenldq-58" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-60" value="Label UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="E6rGj8i0a1SSwwkenldq-58" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-64" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="E6rGj8i0a1SSwwkenldq-58" target="LJFPJaAqwbhQFGvEF_o8-57" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="E6rGj8i0a1SSwwkenldq-65" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="E6rGj8i0a1SSwwkenldq-55" target="qAa2Pi7rPlZP1lqOzIKF-38" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-1" value="&lt;u&gt;ProjectBoard&lt;/u&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#3333FF;" parent="1" vertex="1">
          <mxGeometry x="130" y="-650" width="180" height="120" as="geometry" />
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-2" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="bdqJI-T08oNJTsnCjI4d-1" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-3" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="bdqJI-T08oNJTsnCjI4d-2" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-4" value="UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="bdqJI-T08oNJTsnCjI4d-2" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-5" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="bdqJI-T08oNJTsnCjI4d-1" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-6" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="bdqJI-T08oNJTsnCjI4d-5" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-7" value="Project UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="bdqJI-T08oNJTsnCjI4d-5" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-8" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="bdqJI-T08oNJTsnCjI4d-1" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-9" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="bdqJI-T08oNJTsnCjI4d-8" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-10" value="Board UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="bdqJI-T08oNJTsnCjI4d-8" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-14" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#007FFF;" parent="1" source="bdqJI-T08oNJTsnCjI4d-5" target="LU-fPexgcIpwWTkRIjDJ-2" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="330" y="-575" />
              <mxPoint x="330" y="-610" />
              <mxPoint x="433" y="-610" />
              <mxPoint x="433" y="-970" />
              <mxPoint x="413" y="-970" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-15" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=-0.006;entryY=0.189;entryDx=0;entryDy=0;entryPerimeter=0;" parent="1" source="bdqJI-T08oNJTsnCjI4d-8" target="qAa2Pi7rPlZP1lqOzIKF-2" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-33" value="&lt;u&gt;TeamPermission&lt;/u&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#FF99FF;" parent="1" vertex="1">
          <mxGeometry x="390" y="-1370" width="180" height="150" as="geometry" />
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-34" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="bdqJI-T08oNJTsnCjI4d-33" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-35" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="bdqJI-T08oNJTsnCjI4d-34" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-36" value="id " style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="bdqJI-T08oNJTsnCjI4d-34" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-37" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="bdqJI-T08oNJTsnCjI4d-33" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-38" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="bdqJI-T08oNJTsnCjI4d-37" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-39" value="permissions" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="bdqJI-T08oNJTsnCjI4d-37" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-40" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="bdqJI-T08oNJTsnCjI4d-33" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-41" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="bdqJI-T08oNJTsnCjI4d-40" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-42" value="Team UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="bdqJI-T08oNJTsnCjI4d-40" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-14" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="bdqJI-T08oNJTsnCjI4d-33" vertex="1">
          <mxGeometry y="120" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-15" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-14" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-16" value="User UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-14" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-43" value="&lt;u&gt;ProjectPermission&lt;/u&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#FF99FF;" parent="1" vertex="1">
          <mxGeometry x="390" y="-1190" width="180" height="150" as="geometry" />
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-44" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="bdqJI-T08oNJTsnCjI4d-43" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-45" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="bdqJI-T08oNJTsnCjI4d-44" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-46" value="id " style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="bdqJI-T08oNJTsnCjI4d-44" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-47" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="bdqJI-T08oNJTsnCjI4d-43" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-48" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="bdqJI-T08oNJTsnCjI4d-47" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-49" value="permissions" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="bdqJI-T08oNJTsnCjI4d-47" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-50" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="bdqJI-T08oNJTsnCjI4d-43" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-51" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="bdqJI-T08oNJTsnCjI4d-50" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-52" value="Project UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="bdqJI-T08oNJTsnCjI4d-50" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-11" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="bdqJI-T08oNJTsnCjI4d-43" vertex="1">
          <mxGeometry y="120" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-12" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-11" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-13" value="User UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-11" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-63" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#CC00CC;exitX=0;exitY=0.5;exitDx=0;exitDy=0;" parent="1" source="bdqJI-T08oNJTsnCjI4d-37" target="Nov7NwWhawipYWJH2YjQ-149" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="390" y="-1290" />
              <mxPoint x="100" y="-1290" />
              <mxPoint x="100" y="-445" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-67" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#990000;" parent="1" source="bdqJI-T08oNJTsnCjI4d-47" target="Nov7NwWhawipYWJH2YjQ-149" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="90" y="-1115" />
              <mxPoint x="90" y="-445" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-68" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="bdqJI-T08oNJTsnCjI4d-50" target="LU-fPexgcIpwWTkRIjDJ-2" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="bdqJI-T08oNJTsnCjI4d-69" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="bdqJI-T08oNJTsnCjI4d-40" target="Nov7NwWhawipYWJH2YjQ-350" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="230" y="-1265" />
              <mxPoint x="230" y="-1505" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-23" value="&lt;u&gt;TeamProjectRelationship&lt;br&gt;&lt;/u&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#67AB9F;" parent="1" vertex="1">
          <mxGeometry x="150" y="-1250" width="180" height="120" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-24" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-23" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-25" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-24" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-26" value="id " style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-24" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-27" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-23" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-28" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-27" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-29" value="Team UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-27" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-30" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-23" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-31" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-30" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-32" value="Project UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-30" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-33" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.991;entryY=0.28;entryDx=0;entryDy=0;entryPerimeter=0;" parent="1" source="7HPgxSEbEwWD8oImPeql-27" target="Nov7NwWhawipYWJH2YjQ-350" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="130" y="-1175" />
              <mxPoint x="130" y="-1320" />
              <mxPoint x="180" y="-1320" />
              <mxPoint x="180" y="-1512" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-34" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="7HPgxSEbEwWD8oImPeql-30" target="LU-fPexgcIpwWTkRIjDJ-2" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-35" value="&lt;u&gt;TeamDevExp&lt;br&gt;&lt;/u&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#67AB9F;" parent="1" vertex="1">
          <mxGeometry x="530" y="-1570" width="300" height="180" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-36" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-35" vertex="1">
          <mxGeometry y="30" width="300" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-37" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-36" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-38" value="id " style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-36" vertex="1">
          <mxGeometry x="40" width="260" height="30" as="geometry">
            <mxRectangle width="260" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-42" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-35" vertex="1">
          <mxGeometry y="60" width="300" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-43" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-42" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-44" value="&lt;u style=&quot;border-color: var(--border-color); font-weight: 700; text-align: center;&quot;&gt;Team UUID&lt;/u&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-42" vertex="1">
          <mxGeometry x="40" width="260" height="30" as="geometry">
            <mxRectangle width="260" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-45" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-35" vertex="1">
          <mxGeometry y="90" width="300" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-46" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-45" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-47" value="&lt;div style=&quot;text-align: center;&quot;&gt;&lt;span style=&quot;background-color: initial;&quot;&gt;&lt;b&gt;&lt;u&gt;created_at&lt;/u&gt;&lt;/b&gt;&lt;/span&gt;&lt;/div&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-45" vertex="1">
          <mxGeometry x="40" width="260" height="30" as="geometry">
            <mxRectangle width="260" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-48" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-35" vertex="1">
          <mxGeometry y="120" width="300" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-49" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-48" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-50" value="&lt;div style=&quot;text-align: center;&quot;&gt;&lt;span style=&quot;background-color: initial;&quot;&gt;&lt;b&gt;&lt;u&gt;deleted_at&lt;/u&gt;&lt;/b&gt;&lt;/span&gt;&lt;/div&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-48" vertex="1">
          <mxGeometry x="40" width="260" height="30" as="geometry">
            <mxRectangle width="260" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-57" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-35" vertex="1">
          <mxGeometry y="150" width="300" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-58" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-57" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-59" value="&lt;u style=&quot;border-color: var(--border-color); font-weight: 700; text-align: center;&quot;&gt;Project UUID&lt;/u&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-57" vertex="1">
          <mxGeometry x="40" width="260" height="30" as="geometry">
            <mxRectangle width="260" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-60" value="&lt;b&gt;UserDevExp&lt;/b&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#FF99FF;" parent="1" vertex="1">
          <mxGeometry x="-750" y="-1295" width="180" height="180" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-61" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-60" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-62" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-61" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-63" value="id " style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-61" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-64" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-60" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-65" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-64" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-66" value="&lt;b style=&quot;border-color: var(--border-color);&quot;&gt;&lt;u style=&quot;border-color: var(--border-color);&quot;&gt;Team UUID&lt;/u&gt;&lt;/b&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-64" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-67" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-60" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-68" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-67" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-69" value="User UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-67" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-70" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-60" vertex="1">
          <mxGeometry y="120" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-71" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-70" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-72" value="created_at" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-70" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-73" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-60" vertex="1">
          <mxGeometry y="150" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-74" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-73" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-75" value="deleted_at" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-73" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-76" value="&lt;u&gt;ProjectInvite&lt;br&gt;&lt;/u&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#67AB9F;" parent="1" vertex="1">
          <mxGeometry x="640" y="-1310" width="180" height="240" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-77" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-76" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-78" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-77" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-79" value="UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-77" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-80" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-76" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-81" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-80" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-82" value="Project UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-80" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-83" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-76" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-84" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-83" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-85" value="team UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-83" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-86" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-76" vertex="1">
          <mxGeometry y="120" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-87" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-86" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-88" value="message" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-86" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-89" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-76" vertex="1">
          <mxGeometry y="150" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-90" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-89" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-91" value="is_accept" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-89" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-92" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-76" vertex="1">
          <mxGeometry y="180" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-93" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-92" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-94" value="is_rejected" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-92" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-95" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-76" vertex="1">
          <mxGeometry y="210" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-96" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-95" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-97" value="created_at" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-95" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-98" value="&lt;u&gt;TeamRequest&lt;br&gt;&lt;/u&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#67AB9F;" parent="1" vertex="1">
          <mxGeometry x="840" y="-1310" width="180" height="240" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-99" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-98" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-100" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-99" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-101" value="UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-99" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-102" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-98" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-103" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-102" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-104" value="Team UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-102" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-105" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-98" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-106" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-105" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-107" value="Project UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-105" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-108" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-98" vertex="1">
          <mxGeometry y="120" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-109" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-108" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-110" value="message" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-108" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-111" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-98" vertex="1">
          <mxGeometry y="150" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-112" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-111" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-113" value="is_accept" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-111" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-114" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-98" vertex="1">
          <mxGeometry y="180" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-115" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-114" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-116" value="is_rejected" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-114" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-117" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="7HPgxSEbEwWD8oImPeql-98" vertex="1">
          <mxGeometry y="210" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-118" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-117" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="7HPgxSEbEwWD8oImPeql-119" value="created_at" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="7HPgxSEbEwWD8oImPeql-117" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="t5vfvvBABVAUMv1XQ9CC-1" value="pr" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#FF99FF;" parent="1" source="7HPgxSEbEwWD8oImPeql-77" target="LU-fPexgcIpwWTkRIjDJ-11" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="640" y="-1240" />
              <mxPoint x="620" y="-1240" />
              <mxPoint x="620" y="-980" />
              <mxPoint x="490" y="-980" />
              <mxPoint x="490" y="-885" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="t5vfvvBABVAUMv1XQ9CC-2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#00CC00;" parent="1" source="7HPgxSEbEwWD8oImPeql-105" target="LU-fPexgcIpwWTkRIjDJ-8" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1120" y="-1205" />
              <mxPoint x="1120" y="-960" />
              <mxPoint x="460" y="-960" />
              <mxPoint x="460" y="-915" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="t5vfvvBABVAUMv1XQ9CC-3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#FF6666;" parent="1" source="7HPgxSEbEwWD8oImPeql-83" target="Nov7NwWhawipYWJH2YjQ-350" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="590" y="-1205" />
              <mxPoint x="590" y="-1380" />
              <mxPoint x="490" y="-1380" />
              <mxPoint x="490" y="-1540" />
              <mxPoint x="180" y="-1540" />
              <mxPoint x="180" y="-1505" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="t5vfvvBABVAUMv1XQ9CC-4" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#0066CC;" parent="1" source="7HPgxSEbEwWD8oImPeql-102" target="Nov7NwWhawipYWJH2YjQ-350" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1120" y="-1235" />
              <mxPoint x="1120" y="-1620" />
              <mxPoint x="240" y="-1620" />
              <mxPoint x="240" y="-1505" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="t5vfvvBABVAUMv1XQ9CC-5" value="&lt;b&gt;TeamTool&lt;/b&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#007FFF;" parent="1" vertex="1">
          <mxGeometry x="-520" y="-1665" width="180" height="90" as="geometry" />
        </mxCell>
        <mxCell id="t5vfvvBABVAUMv1XQ9CC-6" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="t5vfvvBABVAUMv1XQ9CC-5" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="t5vfvvBABVAUMv1XQ9CC-7" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="t5vfvvBABVAUMv1XQ9CC-6" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="t5vfvvBABVAUMv1XQ9CC-8" value="id" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="t5vfvvBABVAUMv1XQ9CC-6" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="t5vfvvBABVAUMv1XQ9CC-12" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="t5vfvvBABVAUMv1XQ9CC-5" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="t5vfvvBABVAUMv1XQ9CC-13" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="t5vfvvBABVAUMv1XQ9CC-12" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="t5vfvvBABVAUMv1XQ9CC-14" value="name" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="t5vfvvBABVAUMv1XQ9CC-12" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="t5vfvvBABVAUMv1XQ9CC-21" value="&lt;b&gt;TeamToolGroup&lt;/b&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#007FFF;" parent="1" vertex="1">
          <mxGeometry x="-300" y="-1680" width="180" height="120" as="geometry" />
        </mxCell>
        <mxCell id="t5vfvvBABVAUMv1XQ9CC-22" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="t5vfvvBABVAUMv1XQ9CC-21" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="t5vfvvBABVAUMv1XQ9CC-23" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="t5vfvvBABVAUMv1XQ9CC-22" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="t5vfvvBABVAUMv1XQ9CC-24" value="UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="t5vfvvBABVAUMv1XQ9CC-22" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="t5vfvvBABVAUMv1XQ9CC-34" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="t5vfvvBABVAUMv1XQ9CC-21" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="t5vfvvBABVAUMv1XQ9CC-35" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="t5vfvvBABVAUMv1XQ9CC-34" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="t5vfvvBABVAUMv1XQ9CC-36" value="Team UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="t5vfvvBABVAUMv1XQ9CC-34" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="t5vfvvBABVAUMv1XQ9CC-37" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="t5vfvvBABVAUMv1XQ9CC-21" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="t5vfvvBABVAUMv1XQ9CC-38" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="t5vfvvBABVAUMv1XQ9CC-37" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="t5vfvvBABVAUMv1XQ9CC-39" value="TeamTool ID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="t5vfvvBABVAUMv1XQ9CC-37" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="t5vfvvBABVAUMv1XQ9CC-40" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="t5vfvvBABVAUMv1XQ9CC-37" target="t5vfvvBABVAUMv1XQ9CC-6" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="t5vfvvBABVAUMv1XQ9CC-41" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" parent="1" source="t5vfvvBABVAUMv1XQ9CC-34" target="Nov7NwWhawipYWJH2YjQ-349" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="cOokgg_9ec5KLx6cwFXG-1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" parent="1" source="7HPgxSEbEwWD8oImPeql-42" target="Nov7NwWhawipYWJH2YjQ-349" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="510" y="-1495" />
              <mxPoint x="510" y="-1560" />
              <mxPoint x="345" y="-1560" />
              <mxPoint x="345" y="-1570" />
              <mxPoint x="100" y="-1570" />
              <mxPoint x="100" y="-1550" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="cOokgg_9ec5KLx6cwFXG-2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" parent="1" source="7HPgxSEbEwWD8oImPeql-57" target="LU-fPexgcIpwWTkRIjDJ-1" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="510" y="-1405" />
              <mxPoint x="510" y="-1380" />
              <mxPoint x="317" y="-1380" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="cOokgg_9ec5KLx6cwFXG-7" value="TeamMemberPosition" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#FF99FF;" parent="1" vertex="1">
          <mxGeometry x="-950" y="-1465" width="180" height="90" as="geometry" />
        </mxCell>
        <mxCell id="cOokgg_9ec5KLx6cwFXG-8" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="cOokgg_9ec5KLx6cwFXG-7" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="cOokgg_9ec5KLx6cwFXG-9" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="cOokgg_9ec5KLx6cwFXG-8" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="cOokgg_9ec5KLx6cwFXG-10" value="id" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="cOokgg_9ec5KLx6cwFXG-8" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="cOokgg_9ec5KLx6cwFXG-11" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="cOokgg_9ec5KLx6cwFXG-7" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="cOokgg_9ec5KLx6cwFXG-12" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="cOokgg_9ec5KLx6cwFXG-11" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="cOokgg_9ec5KLx6cwFXG-13" value="position" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="cOokgg_9ec5KLx6cwFXG-11" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="cOokgg_9ec5KLx6cwFXG-14" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="cOokgg_9ec5KLx6cwFXG-4" target="cOokgg_9ec5KLx6cwFXG-8" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="gl-DomWW6gSfC4Fig_aY-1" value="&lt;b&gt;&lt;u&gt;Competence&lt;/u&gt;&lt;/b&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#00CC00;" parent="1" vertex="1">
          <mxGeometry x="-1060" y="-635" width="180" height="90" as="geometry" />
        </mxCell>
        <mxCell id="gl-DomWW6gSfC4Fig_aY-2" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="gl-DomWW6gSfC4Fig_aY-1" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="gl-DomWW6gSfC4Fig_aY-3" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="gl-DomWW6gSfC4Fig_aY-2" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="gl-DomWW6gSfC4Fig_aY-4" value="id " style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="gl-DomWW6gSfC4Fig_aY-2" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="gl-DomWW6gSfC4Fig_aY-5" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="gl-DomWW6gSfC4Fig_aY-1" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="gl-DomWW6gSfC4Fig_aY-6" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="gl-DomWW6gSfC4Fig_aY-5" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="gl-DomWW6gSfC4Fig_aY-7" value="competence" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="gl-DomWW6gSfC4Fig_aY-5" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="gl-DomWW6gSfC4Fig_aY-14" value="&lt;b&gt;&lt;u&gt;CompetenceGroup&lt;/u&gt;&lt;/b&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#00CC00;" parent="1" vertex="1">
          <mxGeometry x="-930" y="-460" width="180" height="120" as="geometry" />
        </mxCell>
        <mxCell id="gl-DomWW6gSfC4Fig_aY-15" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="gl-DomWW6gSfC4Fig_aY-14" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="gl-DomWW6gSfC4Fig_aY-16" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="gl-DomWW6gSfC4Fig_aY-15" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="gl-DomWW6gSfC4Fig_aY-17" value="id " style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="gl-DomWW6gSfC4Fig_aY-15" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="gl-DomWW6gSfC4Fig_aY-18" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="gl-DomWW6gSfC4Fig_aY-14" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="gl-DomWW6gSfC4Fig_aY-19" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="gl-DomWW6gSfC4Fig_aY-18" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="gl-DomWW6gSfC4Fig_aY-20" value="competence id" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="gl-DomWW6gSfC4Fig_aY-18" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="gl-DomWW6gSfC4Fig_aY-21" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="gl-DomWW6gSfC4Fig_aY-14" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="gl-DomWW6gSfC4Fig_aY-22" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="gl-DomWW6gSfC4Fig_aY-21" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="gl-DomWW6gSfC4Fig_aY-23" value="personal_info id" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="gl-DomWW6gSfC4Fig_aY-21" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="gl-DomWW6gSfC4Fig_aY-24" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="gl-DomWW6gSfC4Fig_aY-21" target="Nov7NwWhawipYWJH2YjQ-46" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="gl-DomWW6gSfC4Fig_aY-25" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" source="gl-DomWW6gSfC4Fig_aY-18" target="gl-DomWW6gSfC4Fig_aY-2" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="gl-DomWW6gSfC4Fig_aY-26" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.938;entryY=0.004;entryDx=0;entryDy=0;entryPerimeter=0;" parent="1" source="7HPgxSEbEwWD8oImPeql-2" target="Nov7NwWhawipYWJH2YjQ-2" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="YDDpKSoIlpt64208BBWw-15" value="&lt;u&gt;Includes&lt;/u&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#FFB570;" parent="1" vertex="1">
          <mxGeometry x="720" y="-60" width="180" height="120" as="geometry" />
        </mxCell>
        <mxCell id="YDDpKSoIlpt64208BBWw-16" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="YDDpKSoIlpt64208BBWw-15" vertex="1">
          <mxGeometry y="30" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="YDDpKSoIlpt64208BBWw-17" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="YDDpKSoIlpt64208BBWw-16" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="YDDpKSoIlpt64208BBWw-18" value="UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="YDDpKSoIlpt64208BBWw-16" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="YDDpKSoIlpt64208BBWw-19" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="YDDpKSoIlpt64208BBWw-15" vertex="1">
          <mxGeometry y="60" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="YDDpKSoIlpt64208BBWw-20" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="YDDpKSoIlpt64208BBWw-19" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="YDDpKSoIlpt64208BBWw-21" value="url" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="YDDpKSoIlpt64208BBWw-19" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="YDDpKSoIlpt64208BBWw-22" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="YDDpKSoIlpt64208BBWw-15" vertex="1">
          <mxGeometry y="90" width="180" height="30" as="geometry" />
        </mxCell>
        <mxCell id="YDDpKSoIlpt64208BBWw-23" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="YDDpKSoIlpt64208BBWw-22" vertex="1">
          <mxGeometry width="40" height="30" as="geometry">
            <mxRectangle width="40" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="YDDpKSoIlpt64208BBWw-24" value="Card UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="YDDpKSoIlpt64208BBWw-22" vertex="1">
          <mxGeometry x="40" width="140" height="30" as="geometry">
            <mxRectangle width="140" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="YDDpKSoIlpt64208BBWw-25" value="" style="endArrow=classic;html=1;rounded=0;exitX=0;exitY=0.5;exitDx=0;exitDy=0;" parent="1" source="YDDpKSoIlpt64208BBWw-22" target="qAa2Pi7rPlZP1lqOzIKF-38" edge="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="610" y="-50" as="sourcePoint" />
            <mxPoint x="660" y="-100" as="targetPoint" />
            <Array as="points">
              <mxPoint x="720" y="-315" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-1" value="&lt;b style=&quot;border-color: var(--border-color);&quot;&gt;&lt;u style=&quot;border-color: var(--border-color);&quot;&gt;Team User Relationship&lt;/u&gt;&lt;/b&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;" parent="1" vertex="1">
          <mxGeometry x="-810" y="-1990" width="225" height="230" as="geometry" />
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-2" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="ZHKatu-EURO-KajZlyEM-1" vertex="1">
          <mxGeometry y="30" width="225" height="30" as="geometry" />
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-3" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="ZHKatu-EURO-KajZlyEM-2" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-4" value="id (UUID)" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="ZHKatu-EURO-KajZlyEM-2" vertex="1">
          <mxGeometry x="70" width="155" height="30" as="geometry">
            <mxRectangle width="155" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-5" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="ZHKatu-EURO-KajZlyEM-1" vertex="1">
          <mxGeometry y="60" width="225" height="20" as="geometry" />
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-6" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="ZHKatu-EURO-KajZlyEM-5" vertex="1">
          <mxGeometry width="70" height="20" as="geometry">
            <mxRectangle width="70" height="20" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-7" value="Team UUID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="ZHKatu-EURO-KajZlyEM-5" vertex="1">
          <mxGeometry x="70" width="155" height="20" as="geometry">
            <mxRectangle width="155" height="20" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-8" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="ZHKatu-EURO-KajZlyEM-1" vertex="1">
          <mxGeometry y="80" width="225" height="30" as="geometry" />
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-9" value="&lt;b&gt;FK&lt;/b&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="ZHKatu-EURO-KajZlyEM-8" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-10" value="&lt;b style=&quot;border-color: var(--border-color);&quot;&gt;&lt;u style=&quot;border-color: var(--border-color);&quot;&gt;User UUID&lt;/u&gt;&lt;/b&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="ZHKatu-EURO-KajZlyEM-8" vertex="1">
          <mxGeometry x="70" width="155" height="30" as="geometry">
            <mxRectangle width="155" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-11" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="ZHKatu-EURO-KajZlyEM-1" vertex="1">
          <mxGeometry y="110" width="225" height="30" as="geometry" />
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-12" value="&lt;b style=&quot;border-color: var(--border-color);&quot;&gt;FK&lt;/b&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="ZHKatu-EURO-KajZlyEM-11" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-13" value="&lt;u style=&quot;border-color: var(--border-color);&quot;&gt;&lt;b style=&quot;border-color: var(--border-color);&quot;&gt;Request UUID&lt;/b&gt;&lt;/u&gt;" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="ZHKatu-EURO-KajZlyEM-11" vertex="1">
          <mxGeometry x="70" width="155" height="30" as="geometry">
            <mxRectangle width="155" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-14" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="ZHKatu-EURO-KajZlyEM-1" vertex="1">
          <mxGeometry y="140" width="225" height="30" as="geometry" />
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-15" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="ZHKatu-EURO-KajZlyEM-14" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-16" value="status" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="ZHKatu-EURO-KajZlyEM-14" vertex="1">
          <mxGeometry x="70" width="155" height="30" as="geometry">
            <mxRectangle width="155" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-17" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="ZHKatu-EURO-KajZlyEM-1" vertex="1">
          <mxGeometry y="170" width="225" height="30" as="geometry" />
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-18" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="ZHKatu-EURO-KajZlyEM-17" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-19" value="is_menti_blocked" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="ZHKatu-EURO-KajZlyEM-17" vertex="1">
          <mxGeometry x="70" width="155" height="30" as="geometry">
            <mxRectangle width="155" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-20" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="ZHKatu-EURO-KajZlyEM-1" vertex="1">
          <mxGeometry y="200" width="225" height="30" as="geometry" />
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-21" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="ZHKatu-EURO-KajZlyEM-20" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-22" value="is_mentor_blocked" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="ZHKatu-EURO-KajZlyEM-20" vertex="1">
          <mxGeometry x="70" width="155" height="30" as="geometry">
            <mxRectangle width="155" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-23" value="&lt;div&gt;status:&lt;/div&gt;&lt;div&gt;-sent&lt;/div&gt;&lt;div&gt;-active&lt;/div&gt;&lt;div&gt;-deleted&lt;br&gt;&lt;/div&gt;&lt;div&gt;-canceled&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;" parent="1" vertex="1">
          <mxGeometry x="-995" y="-1920" width="130" height="90" as="geometry" />
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-24" value="&lt;b&gt;&lt;u&gt;Request&lt;/u&gt;&lt;/b&gt;" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;fillColor=#ffffff;strokeColor=#000000;" parent="1" vertex="1">
          <mxGeometry x="-510" y="-1990" width="220" height="150" as="geometry" />
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-25" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="ZHKatu-EURO-KajZlyEM-24" vertex="1">
          <mxGeometry y="30" width="220" height="30" as="geometry" />
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-26" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="ZHKatu-EURO-KajZlyEM-25" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-27" value="id (UUID)" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;html=1;whiteSpace=wrap;" parent="ZHKatu-EURO-KajZlyEM-25" vertex="1">
          <mxGeometry x="70" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-28" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="ZHKatu-EURO-KajZlyEM-24" vertex="1">
          <mxGeometry y="60" width="220" height="30" as="geometry" />
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-29" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="ZHKatu-EURO-KajZlyEM-28" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-30" value="created_date" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="ZHKatu-EURO-KajZlyEM-28" vertex="1">
          <mxGeometry x="70" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-31" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="ZHKatu-EURO-KajZlyEM-24" vertex="1">
          <mxGeometry y="90" width="220" height="30" as="geometry" />
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-32" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="ZHKatu-EURO-KajZlyEM-31" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-33" value="closed_date" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="ZHKatu-EURO-KajZlyEM-31" vertex="1">
          <mxGeometry x="70" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-34" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;html=1;" parent="ZHKatu-EURO-KajZlyEM-24" vertex="1">
          <mxGeometry y="120" width="220" height="30" as="geometry" />
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-35" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;html=1;whiteSpace=wrap;" parent="ZHKatu-EURO-KajZlyEM-34" vertex="1">
          <mxGeometry width="70" height="30" as="geometry">
            <mxRectangle width="70" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZHKatu-EURO-KajZlyEM-36" value="request_sender_uuid" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;html=1;whiteSpace=wrap;" parent="ZHKatu-EURO-KajZlyEM-34" vertex="1">
          <mxGeometry x="70" width="150" height="30" as="geometry">
            <mxRectangle width="150" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="h8cYAdCCjP3ndByas5WN-1" value="" style="shape=note;whiteSpace=wrap;html=1;backgroundOutline=1;fontColor=#000000;darkOpacity=0.05;fillColor=#FFF9B2;strokeColor=none;fillStyle=solid;direction=west;gradientDirection=north;gradientColor=#FFF2A1;shadow=1;size=20;pointerEvents=1;" vertex="1" parent="1">
          <mxGeometry x="110" y="-860" width="140" height="160" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>




## Используемы инструменты

- python - 3.11
- fastapi - 0.100.0
- sqlalchemy - 2.0.18
- postgres - 15.3
- docker compose - 3.9
