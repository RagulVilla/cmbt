import requests
import pandas as pd

def fetch_data_from_api(api_url):
    """Fetches data from the given API URL."""
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data. HTTP Status Code: {response.status_code}")

def save_data_to_excel(data, file_name):
    """Saves a list of dictionaries to an Excel file."""
    # Convert data to a Pandas DataFrame
    df = pd.DataFrame(data)
    # Save DataFrame to an Excel file
    df.to_excel(file_name, index=False)
    print(f"Data successfully saved to {file_name}")

def main():
    # API endpoint to fetch data from
    api_url = "https://jsonplaceholder.typicode.com/users"
    excel_file = "users_data.xlsx"
    
    print("Fetching data from API...")
    data = fetch_data_from_api(api_url)
    
    print(f"Data fetched successfully! Total records: {len(data)}")
    print("Saving data to Excel...")
    save_data_to_excel(data, excel_file)

if __name__ == "__main__":
    main()
