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

## Генераторы

### filter_by_currency(transactions, currency)
Фильтрует транзакции по валюте.

### transaction_descriptions(transactions)  
Возвращает описания транзакций.

### card_number_generator(start, end)
Генерирует номера карт в диапазоне.

## Генерация HTML отчёта покрытия

```powershell
pytest --cov=src --cov-report=html tests/
```

## Декораторы

### `@log(filename=None)`
Декоратор для логирования выполнения функций.

```python
from src.decorators.decorators import log

@log()
def add(a, b):
    return a + b

@log(filename="operations.log")
def multiply(x, y):
    return x * y
```



