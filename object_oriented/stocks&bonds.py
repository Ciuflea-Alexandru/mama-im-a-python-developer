# Define a series of classes that represent a set of stocks and bonds

from abc import ABC, abstractmethod

class Asset(ABC):
    def __init__(self, price):
        self.price = price

    @abstractmethod
    def get_description():
        pass

class Stock(Asset):
    def __init__(self, ticker, price, description):
        super().__init__(price)
        self.ticker = ticker
        self.description = description
    
    def get_description(self):
        return f'{self.ticker}: {self.description} -- ${self.price}'

class Bond(Asset):
    def __init__(self, price, description, duration, interest):
        super().__init__(price)
        self.description = description
        self.duration = duration
        self.interest = interest
    
    def get_description(self):
        return f'{self.description}: {self.duration} : {self.price}$ : {self.interest}% '
    
ticker = "RHM.DE"
price = 1213.40
description = "Rheinmetall AG"
bondname = "Rheinmetall AG 1.875% 07-FEB-2028"
bondprice = 430.000
duration = 1.75
interest = 1.875

stock = Stock(ticker, price, description)
stock_description = stock.get_description()

bond = Bond(bondprice, bondname, duration, interest)
bond_description = bond.get_description()

print(stock_description)
print(bond_description)