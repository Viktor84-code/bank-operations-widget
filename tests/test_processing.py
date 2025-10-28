import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state():
    sample_data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "PENDING"},
        {"id": 3, "state": "EXECUTED"}
    ]
    result = filter_by_state(sample_data)
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


def test_sort_by_date():
    """Тестируем сортировку по дате"""
    sample_data = [
        {"id": 1, "date": "2023-01-01"},
        {"id": 2, "date": "2022-01-01"},
        {"id": 3, "date": "2024-01-01"}
    ]

    result = sort_by_date(sample_data)

    # Проверяем сортировку по убыванию (новые сверху)
    assert result[0]["id"] == 3  # 2024
    assert result[1]["id"] == 1  # 2023
    assert result[2]["id"] == 2  # 2022


@pytest.mark.parametrize("state,expected_count", [
    ("EXECUTED", 2),
    ("CANCELED", 0),
    ("PENDING", 1)
])
def test_filter_by_state_parametrized(state, expected_count):
    sample_data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "PENDING"},
        {"id": 3, "state": "EXECUTED"}
    ]

    result = filter_by_state(sample_data, state)
    assert len(result) == expected_count