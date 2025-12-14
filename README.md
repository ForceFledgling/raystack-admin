# Raystack Admin

Административный интерфейс для фреймворка Raystack.

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
from raystack_admin import router as admin_router

app.include_router(admin_router)
```

## Структура

- `src/raystack_admin/` - основной код пакета
- `src/raystack_admin/templates/admin/` - шаблоны административного интерфейса
