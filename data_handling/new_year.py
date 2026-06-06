# find out how many days until the year ends

from datetime import date

def days_until_new_year():
    today = date.today()
    new_year = date(today.year + 1, 1, 1)
    
    delta = new_year - today
    
    print(f"Today's date is: {today}")
    print(f"There are {delta.days} days remaining until January 1st, {new_year.year}.")

if __name__ == "__main__":
    days_until_new_year()