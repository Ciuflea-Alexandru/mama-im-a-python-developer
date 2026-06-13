# fetch data from a public API

import requests

def fetch_data(url):
    try:
        # Sending a GET request to the specified URL
        response = requests.get(url, timeout=10)
        
        # This will raise an HTTPError if the response code was 4xx or 5xx
        response.raise_for_status()
        
        # Assuming the response is in JSON format
        data = response.json()
        print("Successfully fetched data:")
        print(data)
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    # Using a free public API for demonstration
    api_url = "https://jsonplaceholder.typicode.com/posts/1"
    fetch_data(api_url)