from src.patterns import process_bank_operations, process_bank_search


def test_process_bank_search():
    """Тест функции поиска операций по строке"""
    test_data = [
        {"description": "Перевод организации", "state": "EXECUTED"},
        {"description": "Оплата услуг", "state": "EXECUTED"},
        {"description": "Открытие вклада", "state": "CANCELED"}
    ]

    result = process_bank_search(test_data, "перевод")
    assert len(result) == 1
    assert result[0]["description"] == "Перевод организации"


def test_process_bank_operations():
    """Тест функции подсчета операций по категориям"""
    test_data = [
        {"description": "Перевод организации"},
        {"description": "Перевод между счетами"},
        {"description": "Оплата услуг"},
        {"description": "Открытие вклада"}
    ]

    categories = ["перевод", "оплата"]
    result = process_bank_operations(test_data, categories)

    assert result["перевод"] == 2
    assert result["оплата"] == 1
