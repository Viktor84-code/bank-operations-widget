import json
from typing import Dict, List


def load_operations(json_path: str) -> List[Dict]:
    """Загружает операции из JSON файла"""
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
