import os
import sys
from unittest.mock import MagicMock, patch

from src.pandas_processing import (load_financial_data, read_csv_data,
                                   read_excel_data)

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

"""
Тесты для модуля pandas_processing с использованием Mock
"""

# Тесты с реальными файлами


def test_read_csv_data_success():
    """Тест успешного чтения CSV файла"""
    file_path = "data/transactions.csv"
    result = read_csv_data(file_path)
    assert result is not None
    assert len(result) == 1000
    assert isinstance(result, list)
    assert isinstance(result[0], dict)


def test_read_excel_data_success():
    """Тест успешного чтения Excel файла"""
    file_path = "data/transactions_excel.xlsx"
    result = read_excel_data(file_path)
    assert result is not None
    assert len(result) == 1000
    assert isinstance(result, list)
    assert isinstance(result[0], dict)


# Тесты с использованием Mock и patch
@patch('src.pandas_processing.pd.read_csv')
def test_read_csv_data_with_mock(mock_read_csv):
    """Тест чтения CSV с использованием Mock"""
    # Arrange - настраиваем mock
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [
        {'id': 1, 'state': 'EXECUTED', 'amount': 100},
        {'id': 2, 'state': 'PENDING', 'amount': 200}
    ]
    mock_read_csv.return_value = mock_df

    # Act
    result = read_csv_data("data/transactions.csv")

    # Assert
    mock_read_csv.assert_called_once_with("data/transactions.csv", delimiter=';')
    assert result == [
        {'id': 1, 'state': 'EXECUTED', 'amount': 100},
        {'id': 2, 'state': 'PENDING', 'amount': 200}
    ]


@patch('src.pandas_processing.pd.read_excel')
def test_read_excel_data_with_mock(mock_read_excel):
    """Тест чтения Excel с использованием Mock"""
    # Arrange
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [
        {'id': 1, 'state': 'EXECUTED', 'amount': 100},
        {'id': 2, 'state': 'PENDING', 'amount': 200}
    ]
    mock_read_excel.return_value = mock_df

    # Act
    result = read_excel_data("data/transactions_excel.xlsx")

    # Assert
    mock_read_excel.assert_called_once_with("data/transactions_excel.xlsx", engine='openpyxl')
    assert result == [
        {'id': 1, 'state': 'EXECUTED', 'amount': 100},
        {'id': 2, 'state': 'PENDING', 'amount': 200}
    ]


def test_load_financial_data():
    """Тест универсальной функции загрузки"""
    # Тестируем загрузку CSV
    csv_result = load_financial_data("data/transactions.csv")
    assert csv_result is not None
    assert len(csv_result) == 1000

    # Тестируем загрузку Excel
    excel_result = load_financial_data("data/transactions_excel.xlsx")
    assert excel_result is not None
    assert len(excel_result) == 1000

    # Тестируем неподдерживаемый формат
    invalid_result = load_financial_data("data/file.txt")
    assert invalid_result is None


def test_read_csv_data_file_not_found():
    """Тест ошибки при чтении CSV"""
    result = read_csv_data("data/nonexistent.csv")
    assert result is None


def test_read_excel_data_file_not_found():
    """Тест ошибки при чтении Excel"""
    result = read_excel_data("data/nonexistent.xlsx")
    assert result is None


@patch('src.pandas_processing.pd.read_csv')
def test_read_csv_data_exception(mock_read_csv):
    """Тест исключения при чтении CSV"""
    # Arrange - настраиваем mock чтобы вызвать исключение
    mock_read_csv.side_effect = Exception("Test error")

    # Act
    result = read_csv_data("data/test.csv")

    # Assert
    assert result is None


@patch('src.pandas_processing.pd.read_excel')
def test_read_excel_data_exception(mock_read_excel):
    """Тест исключения при чтении Excel"""
    # Arrange - настраиваем mock чтобы вызвать исключение
    mock_read_excel.side_effect = Exception("Test error")

    # Act
    result = read_excel_data("data/test.xlsx")

    # Assert
    assert result is None
