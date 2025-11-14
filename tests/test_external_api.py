from unittest.mock import Mock, patch

from src.external_api import convert_amount_to_rub


def test_convert_amount_to_rub_rub():
    """Тест конвертации RUB в RUB"""
    transaction = {"amount": 100.0, "currency": "RUB"}
    result = convert_amount_to_rub(transaction)
    assert result == 100.0


def test_convert_amount_to_rub_usd_with_mock():
    """Тест конвертации USD в RUB с моком API"""
    with patch('src.external_api.requests.get') as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "rates": {"RUB": 80.0}
        }
        mock_get.return_value = mock_response

        transaction = {"amount": 100.0, "currency": "USD"}
        result = convert_amount_to_rub(transaction)
        assert result == 8000.0


def test_convert_amount_to_rub_api_fallback():
    """Тест fallback при ошибке API"""
    with patch('src.external_api.requests.get') as mock_get:
        mock_response = Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        transaction = {"amount": 100.0, "currency": "USD"}
        result = convert_amount_to_rub(transaction)
        assert result == 100.0
