import pandas as pd

print("=== ПРОВЕРКА ДАННЫХ ===")

# Проверяем CSV
df_csv = pd.read_csv('data/transactions.csv', delimiter=';')
print(f"CSV: {len(df_csv)} строк, колонки: {list(df_csv.columns)}")

# Проверяем Excel
df_excel = pd.read_excel('data/transactions_excel.xlsx', engine='openpyxl')
print(f"Excel: {len(df_excel)} строк, колонки: {list(df_excel.columns)}")
