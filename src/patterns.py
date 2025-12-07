import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Фильтрует операции по строке поиска в описании
    с использованием регулярных выражений
    """
    result = []
    for operation in data:
        # Используем re.search для поиска подстроки без учета регистра
        if re.search(search, operation['description'], re.IGNORECASE):
            result.append(operation)
    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Подсчитывает количество операций по категориям с использованием Counter
    """
    counts: Counter[str] = Counter()  # ← ДОБАВЛЯЕМ АННОТАЦИЮ ТИПА

    for operation in data:
        description = operation['description'].lower()
        for category in categories:
            # Используем регулярку для поиска категории в описании
            if re.search(category.lower(), description):
                counts[category] += 1

    return dict(counts)
