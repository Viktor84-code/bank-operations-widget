from src.widget import get_date, mask_account_card


def test_mask_account_card():
    """Тестируем маскировку карт и счетов"""
    # Тест для карты
    card_result = mask_account_card("Visa Platinum 7000792289606361")
    assert card_result == "Visa Platinum 7000 79** **** 6361"

    # Тест для счета
    account_result = mask_account_card("Счет 73654108430135874305")
    assert account_result == "Счет **4305"


def test_get_date():
    """Тестируем преобразование даты"""
    result = get_date("2024-03-11T02:26:18.671407")
    assert result == "11.03.2024"