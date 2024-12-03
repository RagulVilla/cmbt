import requests
import pandas as pd
from pprint import pprint
import time
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set up API key and URL parameters
api_key = os.getenv("apikey")
symbol = "BTC"
market = "USD"
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={symbol}&to_currency={market}&apikey={api_key}"

while True:
    try:
        # Fetch data from API
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        # Print the data for verification
        pprint(data)

        # Extract exchange rate data
        exchange_rate_data = data.get('Realtime Currency Exchange Rate', {})
        
        if exchange_rate_data:
            # Convert JSON data to a DataFrame
            df = pd.DataFrame([exchange_rate_data])

            # Save DataFrame to Excel file
            excel_file_path = 'exchange_rate_data.xlsx'
            df.to_excel(excel_file_path, index=False)

            print(f"Data saved to {excel_file_path}")
        else:
            print("No exchange rate data found.")

    except Exception as e:
        print(f"An error occurred: {e}")

    # Wait for 60 seconds before the next request
    time.sleep(60)