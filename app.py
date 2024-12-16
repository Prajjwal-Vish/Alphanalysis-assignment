import pandas as pd
import os
import yfinance as yf
from get_valid_dates import get_valid_dates
from fetch_stock_data import fetch_stock_data
from tqdm import tqdm  # Optional for progress tracking

# Loading data
data = pd.read_csv(r"C:\Users\prajjwal\Desktop\alphanalysis assignment\data\Stocks.csv")
amount = float(input("Enter Amount : "))  # Taking user input for amount
start_date, end_date = get_valid_dates()  # Taking user input for start and end dates

# Checking if same parameters have been passed before 
file_name = f"data_from_{start_date}_to_{end_date}_amount={amount}.xlsx"
base_dir = r"C:\Users\prajjwal\Desktop\alphanalysis assignment\data"
file_path = os.path.join(base_dir, file_name)


if os.path.exists(file_path):
    print(f"File with same parameter already exists as '{file_name}' at location '{base_dir}'. Data not saved again.")
else:
    # Assigning the flag (new_parameters) to be false
    new_parameters = False
    # Preparing tickers and weightage
    tickers = data['Ticker'].tolist()
    weightage = data.set_index('Ticker')['Weightage'].to_dict()

    # Creating dynamic date columns
    date_columns = pd.date_range(start=start_date, end=end_date).strftime('%Y-%m-%d').tolist()

    # Fetching stock data
    stock_data = fetch_stock_data(tickers, start_date, end_date)

    # Collecting rows efficiently
    rows = []
    for ticker in tqdm(tickers, desc="Fetching stock data and processing"):
        row = {'Ticker': ticker, 'Weightage': weightage.get(ticker, 0)}
        if ticker in stock_data:
            stock_prices = stock_data[ticker].rename(index=lambda x: x.strftime('%Y-%m-%d'))
        else:
            stock_prices = {}
        for date in date_columns:
            row[date] = stock_prices.get(date, None)
        rows.append(row)

    # Creating the DataFrame
    result_df = pd.DataFrame(rows)

    # Calculating number of stocks (vectorized)
    final_result = result_df.copy()
    final_result[date_columns] = (amount * final_result['Weightage'].values[:, None]) / final_result[date_columns]

    # # Droping columns where all values are NaN
    # final_result = final_result.dropna(axis=1, how='all')
    
    # Saving to Excel
    final_result.to_excel(file_path, index=False)
    print(f"File saved successfully as '{file_name}'.")