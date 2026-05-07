# Image Service

Микросервис для загрузки, просмотра и удаления изображений через HTML-интерфейс.

Проект реализован на Django, использует PostgreSQL, запускается через Docker Compose и покрыт тестами.

## Функциональность

Сервис позволяет:

- загружать изображения форматов различных форматов;
- просматривать загруженные изображения на отдельной HTML-странице;
- удалять изображения;
- работать с изображениями через отдельные страницы;
- переходить между страницами через навигационное меню;
- вести логирование;
- запускать приложение и базу данных в отдельных Docker-контейнерах.

## Стек

- Python
- Django
- PostgreSQL
- Docker
- Docker Compose
- Pytest
- pytest-django
- pytest-cov
- Pillow
- python-dotenv / django-environ

## Структура проекта

```text
project/
├── backend/
│   ├── config/
│   │   ├── asgi.py
│   │   ├── logging.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │ 
│   ├── images/
│   │   ├── migrations/
│   │   │
│   │   ├── static/
│   │   │   ├── css/
│   │   │   │   └── images.css
│   │   │   │
│   │   │   └── logos/
│   │   │       ├── cloud.png
│   │   │       ├── franco.gif
│   │   │       ├── magnifying_glas.gif
│   │   │       ├── PY-410_DB.jpg
│   │   │       ├── tobi.jpeg
│   │   │       ├── tom.gif
│   │   │       └── vacuum_cleaner.gif
│   │   │
│   │   ├── templates/
│   │   │   └── images/
│   │   │       ├── db_model.html
│   │   │       ├── delete_detail_image.html
│   │   │       ├── delete_image.html
│   │   │       ├── get_detail_image.html
│   │   │       ├── get_image.html
│   │   │       ├── layout.html
│   │   │       ├── main_page.html
│   │   │       ├── not_found.html
│   │   │       ├── success_add.html
│   │   │       └── upload_image.html
│   │   │
│   │   ├── views/
│   │   │   ├── common_views.py
│   │   │   ├── delete_views.py
│   │   │   ├── get_views.py
│   │   │   └── upload_views.py
│   │   │
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   └── urls.py
│   │ 
│   ├── logs/
│   │ 
│   ├── media/
│   │   └── uploads/
│   │
│   ├── tests/
│   │   ├── test_delete.py
│   │   ├── test_get.py
│   │   ├── test_models.py
│   │   ├── test_upload.py
│   │   └── test_files/
│   │
│   ├── .coverage
│   ├── manage.py
│   └── pytest.ini
│   
├── docker/
│   └── django/
│       └── Dockerfile
│   
├── .env
├── .env.example
├── .gitignore
├── docker-compose.yml
├── notes.md
├── README.md
└── requirements.txt