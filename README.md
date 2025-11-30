# Bank Operations Widget

Project for working with bank operations.

## Functions

### Main Functions
- filter_by_state() - filter operations by status
- sort_by_date() - sort operations by date
- Mask card and account numbers

### New Functions (CSV/Excel Data Reading)
- read_csv_data() - read data from CSV files using pandas
- read_excel_data() - read data from Excel files using pandas
- load_financial_data() - universal data loading from CSV or Excel

## Installation
1. Clone the repository
2. Install dependencies: pip install -r requirements.txt

## Usage
from src.processing import filter_by_state, sort_by_date
from src.pandas_processing import load_financial_data

Load data from CSV/Excel
operations = load_financial_data("data/transactions.csv")

Filter and sort
filtered_operations = filter_by_state(operations, "EXECUTED")
sorted_operations = sort_by_date(filtered_operations)
## 🆕 Новая функциональность (Регулярные выражения)

### Функции для работы с банковскими операциями:

#### `process_bank_search(data, search_str)`
- **Назначение**: Поиск операций по строке в описании
- **Параметры**: 
  - `data: List[Dict]` - список операций
  - `search_str: str` - строка для поиска
- **Возвращает**: `List[Dict]` - отфильтрованный список операций
- **Особенности**: Использует регулярные выражения (`re`) для регистронезависимого поиска

#### `process_bank_operations(data, categories)`
- **Назначение**: Подсчет операций по категориям
- **Параметры**:
  - `data: List[Dict]` - список операций  
  - `categories: List[str]` - список категорий для подсчета
- **Возвращает**: `Dict[str, int]` - словарь {категория: количество}
- **Особенности**: Использует `Counter` из collections

### Основная программа (`main.py`)
- Полноценный пользовательский интерфейс
- Фильтрация по статусу, дате, валюте
- Поиск по описанию с использованием регулярных выражений
- Сортировка и вывод результатов
- 