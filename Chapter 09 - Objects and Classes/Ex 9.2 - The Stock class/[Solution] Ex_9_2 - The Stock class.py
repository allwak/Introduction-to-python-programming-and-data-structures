# (The Stock class) Design a class named Stock to represent a company’s stock that contains:
# A private string data field named symbol for the stock’s symbol.
# A private string data field named name for the stock’s name.
# A private float data field named previousClosingPrice that stores the stock price for the previous day.
# A private float data field named currentPrice that stores the stock price for the current time.
# A constructor that creates a stock with the specified symbol, name, previous price, and current price.
# A getter method for returning the stock name.
# A getter method for returning the stock symbol.
# Getter and setter methods for getting/setting the stock’s previous price.
# Getter and setter methods for getting/setting the stock’s current price.
# A method named getChangePercent() that returns the percentage changed from previousClosingPrice to currentPrice.
# Draw the UML diagram for the class, and then implement the class. 
# Write a test program that creates a Stock object with the stock symbol INTC, 
# the name Intel Corporation, the previous closing price of 20.5, 
# and the new current price of 20.35, and display the price-change percentage.

class Stock:
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.symbol = symbol
        self.name = name
        self.previousClosingPrice = previousClosingPrice
        self.currentPrice = currentPrice
    
    def getName(self):
        return self.name
    
    def getSymbol(self):
        return self.symbol
    
    def getPreviousClosingPrice(self):
        return self.previousClosingPrice
    
    def setPreviousClosingPrice(self, previousClosingPrice):
        self.previousClosingPrice = previousClosingPrice
    
    def getCurrentPrice(self):
        return self.currentPrice
    
    def setCurrentPrice(self, currentPrice):
        self.currentPrice = currentPrice
    
    def getChangePercent(self):
        return (self.currentPrice - self.previousClosingPrice) / self.previousClosingPrice * 100

# -0.7
# The price change is -0.73%
some_stock = Stock("INTC", "Intel Corporation", 20.5, 20.35)
print(some_stock.getChangePercent())