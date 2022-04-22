# Exercise 9.2 - The Stock class

<img src="https://github.com/allwak/Introduction-to-python-programming-and-data-structures/blob/main/Chapter%2009%20-%20Objects%20and%20Classes/Ex%209.2%20-%20The%20Stock%20class/Task.jpg" /> 

# Solution
```python
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

```