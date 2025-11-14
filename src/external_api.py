import os
from typing import Dict

import requests
from dotenv import load_dotenv


def convert_amount_to_rub(transaction: Dict) -> float:
    """Конвертирует сумму транзакции в рубли"""
    load_dotenv()

    amount = float(transaction.get("amount", 0))
    currency = transaction.get("currency", "RUB")

    if currency == "RUB":
        return amount

    api_key = os.getenv("EXCHANGE_RATE_API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}"

    headers = {"apikey": api_key}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            rub_rate = data["rates"].get("RUB", 1.0)
            return amount * rub_rate
        else:
            return amount
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
        return amount
