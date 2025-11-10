import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01"},
        {"id": 2, "state": "PENDING", "date": "2022-01-01"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-01"}
    ]


def test_filter_by_state(sample_operations):
    """Тестируем фильтрацию по статусу"""
    result = filter_by_state(sample_operations)
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


def test_sort_by_date(sample_operations):
    """Тестируем сортировку по дате"""
    result = sort_by_date(sample_operations)
    assert result[0]["id"] == 3  # 2024
    assert result[1]["id"] == 1  # 2023
    assert result[2]["id"] == 2  # 2022
