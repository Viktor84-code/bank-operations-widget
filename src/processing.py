def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список операций по статусу."""
    return [op for op in operations if op.get("state") == state]