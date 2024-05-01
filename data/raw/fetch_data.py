import yfinance as yf

def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetches historical stock data for the given ticker between start_date and end_date using yfinance.
    """
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        print(f"Data fetched for {ticker} from {start_date} to {end_date}")
        return data
    except Exception as e:
        print(f"Failed to fetch data for {ticker}: {str(e)}")
        return None

if __name__ == "__main__":
    # Example usage
    ticker = 'AAPL'
    start_date = '2020-01-01'
    end_date = '2021-01-01'
    data = fetch_stock_data(ticker, start_date, end_date)
    if data is not None:
        data.to_csv(f'{ticker}_{start_date.replace("-", "")}_{end_date.replace("-", "")}.csv')
        print("Data saved to CSV.")
