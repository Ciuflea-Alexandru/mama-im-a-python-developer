# Define a class to represent a stock symbol

class Stock:
    def __init__(self, ticker, price, company):
        self.ticker = ticker
        self.price = price
        self.company = company
    
    def get_description(self):
        return f'{self.ticker}: {self.company} -- ${self.price}'
    
ticker = "RHM.DE"
price = 1213.40
company = "Rheinmetall AG"

symbol = Stock(ticker, price, company)

description = symbol.get_description()
print(description)