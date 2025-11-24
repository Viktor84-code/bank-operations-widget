import logging

# НАСТРОЙКА ЛОГГЕРА ДЛЯ MASKS
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/masks.log', mode='w', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

"""Модуль для маскировки банковских карт и счетов."""

logger = logging.getLogger('masks.account')


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.
    """
    logger.info(f"Маскировка номера карты: {card_number}")

    if not card_number.isdigit() or len(card_number) != 16:
        logger.error(f"Неверный номер карты: {card_number}")
        raise ValueError("Номер карты должен содержать 16 цифр")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета в формате **XXXX.
    """
    logger.info(f"Маскировка номера счета: {account_number}")

    if not account_number.isdigit() or len(account_number) != 20:
        logger.error(f"Неверный номер счета: {account_number}")
        raise ValueError("Номер счета должен содержать 20 цифр")

    masked = f"**{account_number[-4:]}"
    logger.info(f"Счет замаскирован: {masked}")
    return masked
