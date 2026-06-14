# fetche the HTML content of a URL and handle potential errors, such as a 404 error or a connection failure.

import urllib.request
import urllib.error

def fetch_url_content(url):
    """
    Fetches the content of a URL and prints it.
    """
    try:
        # Sending a GET request to the URL
        with urllib.request.urlopen(url) as response:
            # Check the status code
            if response.status == 200:
                # Read the response and decode it from bytes to string
                data = response.read().decode('utf-8')
                print(f"Successfully fetched {len(data)} characters.")
                print("--- First 200 characters ---")
                print(data[:200])
            else:
                print(f"Request failed with status: {response.status}")
                
    except urllib.error.HTTPError as e:
        print(f"HTTP Error occurred: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error occurred: {e.reason}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    target_url = "https://www.python.org"
    fetch_url_content(target_url)