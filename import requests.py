import requests
from pprint import pprint
# Define the URL and parameters
url = "https://www.alphavantage.co/query"
params = {
    "function": "CURRENCY_EXCHANGE_RATE",
    "from_currency": "BTC",
    "to_currency": "USD",
    "apikey": "your_api_key"
}

# Send the GET request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Print the response JSON
    data = response.json()
    
    # Check if 'Realtime Currency Exchange Rate' exists in the response
    if "Realtime Currency Exchange Rate" in data:
        # Access and print the exchange rate
        exchange_rate = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        print(f"Exchange Rate: {exchange_rate}")
    else:
        print("Error: 'Realtime Currency Exchange Rate' not found in the response.")
else:
    print(f"Error: Failed to retrieve data. Status code: {response.status_code}")

pprint(data['Realtime Currency Exchange Rate']['8. Bid Price'])
