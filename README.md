# Raystack Admin

Административный интерфейс и система аутентификации для фреймворка Raystack.

## Установка

```bash
pip install raystack-admin
```

## Использование

### 1. Добавьте шаблоны в настройки

В файле `config/settings.py` добавьте путь к шаблонам админки:

```python
from raystack_admin import get_template_dir

TEMPLATES = [
    {
        "BACKEND": "raystack.template.backends.jinja2.Jinja2",
        "DIRS": [
            "templates",
            get_template_dir(),  # Добавьте эту строку
        ],
        # ... остальные настройки
    }
]
```

### 2. Подключите роутер админки

```python
from raystack_admin import router

app.include_router(router)
```

Роутер включает:
- `/admin/*` - административный интерфейс
- `/users/*` - управление пользователями
- `/groups/*` - управление группами
- `/accounts/*` - аутентификация и регистрация

### 3. Использование моделей и утилит

```python
from raystack_admin import UserModel, GroupModel, User, Group

# Использование моделей
users = await UserModel.objects.all().execute()
groups = await GroupModel.objects.all().execute()
```

## Структура

- `src/raystack_admin/` - основной код пакета
  - `admin/` - административный интерфейс
  - `auth/` - система аутентификации (users, groups, accounts)
  - `templates/` - шаблоны (admin, accounts, registration, pages)
  - `static/` - статические файлы
