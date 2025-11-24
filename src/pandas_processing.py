"""
Модуль для работы с CSV и Excel файлами через Pandas
Домашнее задание 13.1
"""

from typing import Any, Dict, List, Optional, cast

import pandas as pd


def read_csv_data(file_path: str) -> Optional[List[Dict[str, Any]]]:
    """
    Читает финансовые операции из CSV-файла
    """
    try:
        df: pd.DataFrame = pd.read_csv(file_path, delimiter=';')
        # Исправляем тип - приводим к List[Dict[str, Any]]
        operations: List[Dict[str, Any]] = cast(List[Dict[str, Any]], df.to_dict('records'))
        return operations
    except Exception as e:
        print(f"Ошибка при чтении CSV файла {file_path}: {e}")
        return None


def read_excel_data(file_path: str) -> Optional[List[Dict[str, Any]]]:
    """
    Читает финансовые операции из XLSX-файла
    """
    try:
        df: pd.DataFrame = pd.read_excel(file_path, engine='openpyxl')
        # Исправляем тип - приводим к List[Dict[str, Any]]
        operations: List[Dict[str, Any]] = cast(List[Dict[str, Any]], df.to_dict('records'))
        return operations
    except Exception as e:
        print(f"Ошибка при чтении Excel файла {file_path}: {e}")
        return None


def load_financial_data(file_path: str) -> Optional[List[Dict[str, Any]]]:
    """
    Универсальная функция для загрузки данных из CSV или XLSX
    """
    if file_path.endswith('.csv'):
        return read_csv_data(file_path)
    elif file_path.endswith('.xlsx'):
        return read_excel_data(file_path)
    else:
        print(f"Неподдерживаемый формат файла: {file_path}")
        return None
