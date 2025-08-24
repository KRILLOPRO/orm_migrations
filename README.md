# ORM Migrations - Школьный сайт

## Описание проекта

Этот проект демонстрирует работу с Django ORM и миграциями. Проект представляет собой сайт школы с возможностью управления учениками и учителями.

## Основные изменения

### До изменений:
- Связь между Student и Teacher была ForeignKey (многие к одному)
- У каждого ученика мог быть только один учитель

### После изменений:
- Связь изменена на ManyToManyField (многие ко многим)
- Теперь у каждого ученика может быть несколько учителей
- У каждого учителя может быть несколько учеников

## Структура проекта

```s
orm_migrations/
├── manage.py
├── requirements.txt
├── school/                    # Основное приложение
│   ├── models.py             # Модели Student и Teacher
│   ├── views.py              # Представления
│   ├── admin.py              # Админка
│   └── migrations/           # Миграции базы данных
├── website/                   # Настройки проекта
│   ├── settings.py           # Настройки Django
│   └── urls.py               # Основные URL
├── templates/                 # Шаблоны
│   └── school/
│       ├── base.html         # Базовый шаблон
│       └── students_list.html # Список учеников
└── static/                    # Статические файлы
```

## Установка и запуск

### 1. Активация виртуального окружения
```bash
cd /Users/kirilllevcenko/Downloads/orm_migrations
source venv/bin/activate
```

### 2. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 3. Применение миграций
```bash
python manage.py migrate
```

### 4. Загрузка тестовых данных
```bash
python manage.py loaddata school_new.json
```

### 5. Создание суперпользователя (опционально)
```bash
python manage.py createsuperuser
```

### 6. Запуск сервера
```bash
python manage.py runserver
```

## Доступ к сайту

- **Главная страница**: http://127.0.0.1:8000/
- **Админка**: http://127.0.0.1:8000/admin/
- **Debug Toolbar**: http://127.0.0.1:8000/__debug__/

## Модели

### Teacher (Учитель)
- `name` - Имя учителя
- `subject` - Предмет
- `students` - Связь с учениками (ManyToMany)

### Student (Ученик)
- `name` - Имя ученика
- `teachers` - Связь с учителями (ManyToMany)
- `group` - Класс

## Оптимизация запросов

В представлении `students_list` используется `prefetch_related('teachers')` для оптимизации SQL-запросов и избежания проблемы N+1 запросов.

## Админка

Настроена удобная админка с:
- Отображением всех учителей ученика
- Подсчетом количества учеников у учителя
- Фильтрацией и поиском

## Технические детали

- Django 5.2.5
- SQLite база данных
- Bootstrap для стилизации
- Django Debug Toolbar для анализа производительности
