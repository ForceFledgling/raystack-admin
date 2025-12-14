# Raystack Admin Example

Пример проекта с административным интерфейсом и системой аутентификации для фреймворка Raystack.

## Структура проекта

```
raystack-admin/
├── apps/
│   └── admin/          # Приложение админки
│       ├── auth/       # Система аутентификации (users, groups, accounts)
│       ├── urls.py     # Роуты админки
│       └── ...
├── config/
│   ├── settings.py      # Настройки проекта
│   └── urls.py          # Главный роутер
├── templates/          # Шаблоны (admin, accounts, registration, pages)
├── static/             # Статические файлы
├── migrations/         # Миграции базы данных
├── manage.py          # Утилита управления
└── run.py             # Запуск приложения
```

## Установка и запуск

### 1. Убедитесь, что raystack установлен

```bash
cd ../raystack
pip install -e .
```

### 2. Запустите миграции

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Создайте суперпользователя (опционально)

```bash
python manage.py createsuperuser
```

### 4. Запустите сервер

```bash
python run.py
```

Или с помощью uvicorn:

```bash
uvicorn run:app --reload
```

## Доступные маршруты

- `/admin/` - административный интерфейс (dashboard, users, groups)
- `/users/*` - API управления пользователями
- `/groups/*` - API управления группами
- `/accounts/*` - аутентификация и регистрация (login, register, password reset)

## Использование моделей

```python
from apps.admin.auth.users.models import UserModel
from apps.admin.auth.groups.models import GroupModel

# Получить всех пользователей
users = await UserModel.objects.all().execute()

# Получить все группы
groups = await GroupModel.objects.all().execute()
```


