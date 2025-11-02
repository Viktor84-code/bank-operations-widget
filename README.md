# Bank Operations Widget

Проект для работы с банковскими операциями.

## Функции

- `filter_by_state()` - фильтрация операций по статусу
- `sort_by_date()` - сортировка операций по дате
- Маскировать номера карт и счетов

## Установка

1. Клонируйте репозиторий
2. Установите зависимости: `pip install -r requirements.txt`

## Использование

```python
from src.processing import filter_by_state, sort_by_date