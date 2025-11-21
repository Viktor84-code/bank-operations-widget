import os

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_amount_to_rub(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции в рубли через APILayer Convert endpoint
    """
    # ИЗВЛЕКАЕМ ДАННЫЕ ИЗ ТРАНЗАКЦИИ
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    api_key = os.getenv("EXCHANGE_RATE_API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/convert?from={currency}&to=RUB&amount={amount}"

    headers = {"apikey": api_key}

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        return float(data["result"])

    except Exception as e:
        print(f"Ошибка API: {e}")
        return 0.0
