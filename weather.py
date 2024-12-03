import requests
import pandas as pd
from pprint import pprint
import time
from dotenv import load_dotenv
import os

def load_api_key():
    """Load the API key from environment variables."""
    load_dotenv()
    return os.getenv("apikey")

def fetch_exchange_rate(api_key, symbol, market):
    """Fetch the exchange rate from Alpha Vantage API."""
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={symbol}&to_currency={market}&apikey={api_key}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

def process_data(data):
    """Extract exchange rate data from the API response."""
    return data.get('Realtime Currency Exchange Rate', {})

def save_to_excel(df, file_path):
    """Save the DataFrame to an Excel file."""
    df.to_excel(file_path, index=False)
    print(f"Data saved to {file_path}")

def main():
    api_key = load_api_key()
    symbol = "BTC"
    market = "USD"
    excel_file_path = 'exchange_rate_data.xlsx'

    while True:
        try:
            # Fetch and process exchange rate data
            data = fetch_exchange_rate(api_key, symbol, market)
            pprint(data)  # Print the data for verification
            
            exchange_rate_data = process_data(data)
            if exchange_rate_data:
                df = pd.DataFrame([exchange_rate_data])
                save_to_excel(df, excel_file_path)
            else:
                print("No exchange rate data found.")

        except Exception as e:
            print(f"An error occurred: {e}")

        # Wait for 60 seconds before the next request
        time.sleep(60)

if __name__ == "__main__":
    main()