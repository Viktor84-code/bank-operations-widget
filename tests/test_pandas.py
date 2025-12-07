import pandas as pd

print("=== ТЕСТ PANDAS ===")
df_csv = pd.read_csv('data/transactions.csv', delimiter=';')
print(f"✅ CSV: {df_csv.shape[0]} строк, {df_csv.shape[1]} колонок")
print(f"📊 Колонки: {list(df_csv.columns)}")
