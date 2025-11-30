# Bank Operations Widget

Project for working with bank operations.

## Functions

### Main Functions
- filter_by_state() - filter operations by status
- sort_by_date() - sort operations by date
- Mask card and account numbers

### New Functions (CSV/Excel Data Reading)
- read_csv_data() - read data from CSV files using pandas
- read_excel_data() - read data from Excel files using pandas
- load_financial_data() - universal data loading from CSV or Excel

## Installation
1. Clone the repository
2. Install dependencies: pip install -r requirements.txt

## Usage
from src.processing import filter_by_state, sort_by_date
from src.pandas_processing import load_financial_data

Load data from CSV/Excel
operations = load_financial_data("data/transactions.csv")

Filter and sort
filtered_operations = filter_by_state(operations, "EXECUTED")
sorted_operations = sort_by_date(filtered_operations)
