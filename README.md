# News Portal

Проект **News Portal** — это новостной портал с возможностью просмотра превью статей и их автоматического перевода на разные языки с помощью Yandex Translate API.

---

## О проекте

- **Backend:** Django REST Framework
- **Frontend:** HTML/CSS/JS (NGINX)
- **Перевод статей:** интеграция с Yandex Cloud Translation API
- **Хранение данных:** PostgreSQL 
- **Контейнеризация:** Docker Compose

---

## Основные возможности

- Просмотр списка новостных превью с заголовком, описанием, изображением и содержимым.
- API для получения превью статей (только GET-запросы).
- Перевод статей на указанный язык с кешированием переведённых версий.
- Административная панель Django для управления статьями и переводами.

---

## Структура проекта

- **homepage** — приложение с моделями и API для превью новостей.
- **news** — приложение для хранения переводов статей и API для перевода.
- **news_portal/urls.py** — маршруты проекта, включая роуты для превью и перевода.
- **docker-compose.yml** — настройка контейнеров для backend и frontend.

---

## Требования

- Docker и Docker Compose
- Yandex Cloud API ключ и ID каталога (folder ID)

---

## Настройка и запуск

1. Клонируйте репозиторий:
2. Создайте файл .env и заполните переменные
3. Запустите контейнеры: docker-compose up --build
- Backend будет доступен по адресу: http://localhost:8000/
- Frontend  — http://localhost:3000/
- Админ-панель: http://localhost:8000/admin/

##  API
Получение списка превью GET http://localhost:8000/api/preview/

## Перевод статьи

POST http://localhost:8000/api/translate-article/{id}/
Content-Type: application/json

{
    "lang": "en"  # или любой другой поддерживаемый язык
}






