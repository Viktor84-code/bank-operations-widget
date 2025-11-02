def filter_by_currency(transactions, currency):
    """Генератор, фильтрующий транзакции по валюте"""
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        currency_info = operation_amount.get("currency", {})
        if currency_info.get("code") == currency:
            yield transaction


def transaction_descriptions(transactions):
    """Генератор описаний транзакций"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, end):
    """Генератор номеров карт в заданном диапазоне"""
    for number in range(start, end + 1):
        yield f"{number:016d}"
