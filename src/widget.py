from src.masks import get_mask_card_number, get_mask_account


from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_info: str) -> str:
    """
    Маскирует номер карты или счёта в строке формата 'Visa Platinum 7000792289606361'
    или 'Счет 73654108430135874305'
    """
    if "Счет" in card_info:
        # Разделяем "Счет" и номер
        parts = card_info.split()
        account_type = parts[0]  # "Счет"
        number = parts[-1]       # номер счёта
        masked_number = get_mask_account(number)
        return f"{account_type} {masked_number}"
    else:
        # Для карт: "Visa Platinum 7000792289606361"
        parts = card_info.split()
        account_type = " ".join(parts[:-1])  # "Visa Platinum"
        number = parts[-1]                   # номер карты
        masked_number = get_mask_card_number(number)
        return f"{account_type} {masked_number}"
