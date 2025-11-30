import re

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
    Подсчитывает количество операций по категориям
    """
    result = {}
    for category in categories:
        # Тут будет логика подсчета
        pass
    return result
