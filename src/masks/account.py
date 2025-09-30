"""Модуль для маскировки банковских карт и счетов."""


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.
    """
    if not card_number.isdigit() or len(card_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета в формате **XXXX.
    """

    if not account_number.isdigit() or len(account_number) != 20:
        raise ValueError("Номер счета должен содержать 20 цифр")
    return f"**{account_number[-4:]}"
