import os

import requests

api_key = os.getenv("EXCHANGE_RATE_API_KEY")
print("Ключ:", api_key)
url = "https://api.apilayer.com/exchangerates_data/latest?base=USD"
headers = {"apikey": api_key}
response = requests.get(url, headers=headers)
print("Статус:", response.status_code)
if response.status_code == 200:
    data = response.json()
    print("Курс USD к RUB:", data['rates']['RUB'])
else:
    print("Ошибка:", response.text)
