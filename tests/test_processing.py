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


import pytest

from src.processing import filter_by_state, sort_by_date  # ← ЭТА СТРОКА ДОЛЖНА БЫТЬ!


@pytest.fixture
def sample_operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01"},
        {"id": 2, "state": "PENDING", "date": "2022-01-01"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-01"}
    ]

    import pytest

    from src.processing import filter_by_state, sort_by_date

    # ФИКСТУРА - генератор тестовых данных
    @pytest.fixture
    def sample_operations():
        return [
            {"id": 1, "state": "EXECUTED", "date": "2023-01-01"},
            {"id": 2, "state": "PENDING", "date": "2022-01-01"},
            {"id": 3, "state": "EXECUTED", "date": "2024-01-01"}
        ]

    # ТЕСТЫ С ФИКСТУРОЙ
    def test_filter_by_state(sample_operations):  # <- фикстура как аргумент
        result = filter_by_state(sample_operations)
        assert len(result) == 2

    def test_sort_by_date(sample_operations):  # <- фикстура как аргумент
        result = sort_by_date(sample_operations)
        assert result[0]["id"] == 3