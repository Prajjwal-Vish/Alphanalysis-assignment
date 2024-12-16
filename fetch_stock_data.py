from datetime import datetime,timedelta
import yfinance as yf
def fetch_stock_data(tickers, start_date, end_date):
    stock_data = {}
    adjusted_end_date = (datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker+".NS")
            stock_data[ticker] = stock.history(start=start_date, end=adjusted_end_date)['Close']
        except Exception as e:
            print(f"Failed to fetch data for {ticker}: {e}")
    return stock_data