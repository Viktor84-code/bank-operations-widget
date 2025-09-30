from src.masks.account import get_mask_card_number, get_mask_account

def test_get_mask_card_number():
    """Тестируем маскировку номера карты."""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"


def test_get_mask_account():
    """Тестируем маскировку номера счета."""
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("12345678901234567890") == "**7890"
