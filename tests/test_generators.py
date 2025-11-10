import pytest
from src.generators.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "operationAmount": {
                "currency": {"code": "USD"}
            },
            "description": "Перевод организации"
        },
        {
            "id": 2,
            "operationAmount": {
                "currency": {"code": "EUR"}
            },
            "description": "Перевод с карты на карту"
        },
        {
            "id": 3,
            "operationAmount": {
                "currency": {"code": "USD"}
            },
            "description": "Оплата услуг"
        }
    ]


def test_filter_by_currency(sample_transactions):
    """Тест фильтрации по валюте"""
    usd_transactions = filter_by_currency(sample_transactions, "USD")

    # Проверяем первую USD транзакцию
    first_usd = next(usd_transactions)
    assert first_usd["id"] == 1

    # Проверяем вторую USD транзакцию
    second_usd = next(usd_transactions)
    assert second_usd["id"] == 3


def test_transaction_descriptions(sample_transactions):
    """Тест генератора описаний"""
    descriptions = transaction_descriptions(sample_transactions)

    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Оплата услуг"


def test_card_number_generator():
    """Тест генератора номеров карт"""
    card_gen = card_number_generator(1, 3)

    assert next(card_gen) == "0000000000000001"
    assert next(card_gen) == "0000000000000002"
    assert next(card_gen) == "0000000000000003"

    @pytest.mark.parametrize("currency, expected_ids", [
        ("USD", [1, 3]),
        ("EUR", [2]),
        ("RUB", []),
    ])
    def test_filter_by_currency_parametrized(sample_transactions, currency, expected_ids):
        """Параметризованный тест фильтрации по разным валютам"""
        filtered = list(filter_by_currency(sample_transactions, currency))
        assert [t["id"] for t in filtered] == expected_ids

    @pytest.mark.parametrize("start, end, expected", [
        (1, 3, ["0000000000000001", "0000000000000002", "0000000000000003"]),
        (10, 12, ["0000000000000010", "0000000000000011", "0000000000000012"]),
    ])
    def test_card_number_generator_parametrized(start, end, expected):
        """Параметризованный тест генератора номеров карт"""
        result = list(card_number_generator(start, end))
        assert result == expected

        @pytest.mark.parametrize("currency, expected_ids", [
            ("USD", [1, 3]),
            ("EUR", [2]),
            ("RUB", []),
        ])
        def test_filter_by_currency_parametrized(sample_transactions, currency, expected_ids):
            """Параметризованный тест фильтрации по разным валютам"""
            filtered = list(filter_by_currency(sample_transactions, currency))
            assert [t["id"] for t in filtered] == expected_ids

        @pytest.mark.parametrize("start, end, expected", [
            (1, 3, ["0000000000000001", "0000000000000002", "0000000000000003"]),
            (10, 12, ["0000000000000010", "0000000000000011", "0000000000000012"]),
        ])
        def test_card_number_generator_parametrized(start, end, expected):
            """Параметризованный тест генератора номеров карт"""
            result = list(card_number_generator(start, end))
            assert result == expected
