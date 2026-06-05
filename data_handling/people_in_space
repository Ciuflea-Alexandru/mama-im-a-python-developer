# Fetch how many people are in space right now

import requests

url = "http://api.open-notify.org/astros.json"

try:
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        print(f"--- People in Space Right Now: {data['number']} ---")
        for person in data['people']:
            print(f"• {person['name']} (onboard the {person['craft']})")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")