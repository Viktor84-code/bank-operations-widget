import json
from unittest.mock import mock_open, patch

from src.utils import load_operations


def test_load_operations_empty_file():
    """Тест загрузки из пустого файла"""
    # Создаем временный пустой файл для теста
    with open('data/empty_test.json', 'w') as f:
        f.write('[]')
    result = load_operations('data/empty_test.json')
    assert result == []


def test_load_operations_file_not_found():
    """Тест загрузки при отсутствии файла"""
    result = load_operations('nonexistent_file.json')
    assert result == []


def test_load_operations_with_mock():
    """Тест загрузки с mock файла"""
    mock_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]

    with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))) as mock_file:
        with patch("json.load") as mock_json:
            mock_json.return_value = mock_data
            result = load_operations('test.json')

            assert result == mock_data
            mock_file.assert_called_once_with('test.json', 'r', encoding='utf-8-sig')


def test_load_operations_invalid_json_with_mock():
    """Тест загрузки с невалидным JSON через mock"""
    with patch("builtins.open", mock_open(read_data="invalid json")):
        with patch("json.load") as mock_json:
            mock_json.side_effect = json.JSONDecodeError("Error", "doc", 0)
            result = load_operations('invalid.json')
            assert result == []
