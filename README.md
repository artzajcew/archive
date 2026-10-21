# Личный архив

Django-проект для хранения личных файлов. Пользователь регистрируется,
создаёт папки и теги, загружает файлы, ищет их и фильтрует по папке или тегу.

## Запуск

```text
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Откройте `http://127.0.0.1:8000/`.

## Структура

- `archive/models.py` — пользовательские папки, теги и файлы;
- `archive/views.py` — страницы и операции CRUD;
- `templates/` — шаблоны с `extends`, `include`-совместимым базовым шаблоном, циклами и условиями;
- `static/` — CSS и JavaScript;
- `sql/` — схема таблиц и 10 примеров SQL-запросов.

Файлы каждого пользователя изолированы: запросы всегда фильтруются по
текущему пользователю.
