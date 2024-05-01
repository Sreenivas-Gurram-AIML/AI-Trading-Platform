import pandas as pd

def clean_and_preprocess(data_path):
    """
    Cleans and preprocesses the stock data.
    """
    try:
        data = pd.read_csv(data_path)
        # Implement cleaning logic: remove NaNs, adjust formats, etc.
        data.dropna(inplace=True)
        print(f"Data cleaned and preprocessed for {data_path}")
        return data
    except Exception as e:
        print(f"Failed to clean and preprocess data: {str(e)}")
        return None

if __name__ == "__main__":
    # Example usage
    data_path = 'AAPL_20200101_20210101.csv'
    data = clean_and_preprocess(data_path)
    if data is not None:
        processed_path = data_path.replace('.csv', '_processed.csv')
        data.to_csv(processed_path)
        print(f"Processed data saved to {processed_path}")
