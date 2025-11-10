from typing import Dict

import requests


def convert_amount_to_rub(transaction: Dict) -> float:
    """Конвертирует сумму транзакции в рубли"""
    amount = float(transaction.get("amount", 0))
    currency = transaction.get("currency", "RUB")

    if currency == "RUB":
        return amount

    # Получаем актуальный курс через API
    response = requests.get(
        "https://api.exchangerate-api.com/v4/latest/USD"
    )
    if response.status_code == 200:
        rates = response.json()["rates"]
        rub_rate = rates.get("RUB", 1.0)  # fallback курс
        return amount * rub_rate
    else:
        # Если API недоступно, возвращаем исходную сумму
        return amount
