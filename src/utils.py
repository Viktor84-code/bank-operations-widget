import json
import logging
from typing import Any, Dict, List  # ← ДОБАВЛЯЕМ Any

# НАСТРОЙКА ЛОГГЕРА ДЛЯ UTILS
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/utils.log', mode='w', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('utils')


def load_operations(file_path: str) -> List[Dict[str, Any]]:  # ← ИСПРАВЛЯЕМ ТИП
    """Загружает транзакции из JSON файла"""
    logger.info(f"Загрузка операций из файла: {file_path}")

    try:
        # Используем utf-8-sig который автоматически удаляет BOM!
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            data = json.load(file)
            logger.info(f"Успешно загружено {len(data)} операций")
            return data if isinstance(data, list) else []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле: {file_path}")
        return []
    except Exception as e:
        logger.error(f"Ошибка при загрузке файла {file_path}: {e}")
        return []
