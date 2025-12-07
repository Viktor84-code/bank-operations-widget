import json
from typing import Any, Dict, List


def filter_by_state(operations: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список операций по статусу.

    Args:
        operations: Список словарей с операциями
        state: Статус для фильтрации (по умолчанию "EXECUTED")

    Returns:
        Отфильтрованный список операций
    """
    return [operation for operation in operations if operation.get("state") == state]


def sort_by_date(operations: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует операции по дате (по умолчанию — от новых к старым).

    Args:
        operations: Список словарей с операциями
        reverse: Порядок сортировки (True - по убыванию, False - по возрастанию)

    Returns:
        Отсортированный список операций
    """
    return sorted(
        operations,
        key=lambda operation: operation.get("date", ""),
        reverse=reverse)


def load_operations(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает операции из JSON файла
    """
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as file:  # ← МЕНЯЕМ НА utf-8-sig
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
