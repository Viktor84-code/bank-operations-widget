import json
from typing import Dict, List


def load_operations(file_path: str) -> List[Dict]:
    """Загружает транзакции из JSON файла"""
    try:
        # Используем utf-8-sig который автоматически удаляет BOM!
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
        return []
