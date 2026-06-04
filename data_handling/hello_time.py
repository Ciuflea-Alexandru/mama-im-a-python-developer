# ask the users name and show him the current time

import datetime

def greet_user():
    # Get user input
    name = input("What is your name? ")
    
    # Get the current time
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    print(f"Hello, {name}! The current time is {current_time}.")

if __name__ == "__main__":
    greet_user()