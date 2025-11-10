from unittest.mock import Mock, patch

from src.external_api import convert_amount_to_rub


def test_convert_amount_to_rub_rub():
    """Тест конвертации RUB в RUB"""
    transaction = {"amount": "100.0", "currency": "RUB"}
    result = convert_amount_to_rub(transaction)
    assert result == 100.0


def test_convert_amount_to_rub_usd():
    """Тест конвертации USD"""
    transaction = {"amount": "100.0", "currency": "USD"}
    result = convert_amount_to_rub(transaction)
    assert result > 0  # Просто проверяем что возвращает число


def test_convert_amount_to_rub_usd_with_mock():
    """Тест конвертации USD с mock API"""
    transaction = {"amount": "100.0", "currency": "USD"}

    with patch('src.external_api.requests.get') as mock_get:
        # Мокаем ответ API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"rates": {"RUB": 90.0}}
        mock_get.return_value = mock_response

        result = convert_amount_to_rub(transaction)
        assert result == 9000.0  # 100 USD * 90 RUB


def test_convert_amount_to_rub_api_fallback():
    """Тест fallback при отсутствии API ключа"""
    transaction = {"amount": "100.0", "currency": "USD"}

    with patch('os.getenv') as mock_getenv:
        with patch('src.external_api.requests.get') as mock_requests:
            mock_getenv.return_value = None  # Нет API ключа
            # Мокаем что API запрос не делается
            mock_requests.get.side_effect = Exception("API should not be called")

            result = convert_amount_to_rub(transaction)
            assert result == 100.0  # Должен вернуть исходную сумму
