from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """
    Маскирует номер карты или счёта в строке формата 'Visa Platinum 7000792289606361'
    или 'Счет 73654108430135874305'
    """
    if "Счет" in card_info:
        # Разделяем "Счет" и номер
        parts = card_info.split()
        account_type = parts[0]  # "Счет"
        number = parts[-1]  # номер счёта
        masked_number = get_mask_account(number)
        return f"{account_type} {masked_number}"
    else:
        # Для карт: "Visa Platinum 7000792289606361"
        parts = card_info.split()
        account_type = " ".join(parts[:-1])  # "Visa Platinum"
        number = parts[-1]  # номер карты
        masked_number = get_mask_card_number(number)
        return f"{account_type} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует дату из формата '2024-03-11T02:26:18.671407' в '11.03.2024'
    """
    # Шаг 1: Разделяем строку по 'T' и берём первую часть (дату)
    date_part = date_string.split("T")[0]

    # Шаг 2: Разделяем дату по '-' на год, месяц, день
    year, month, day = date_part.split("-")

    # Шаг 3: Собираем в формате ДД.ММ.ГГГГ
    return f"{day}.{month}.{year}"
