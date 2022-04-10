# Exercise 9.1 - The Rectangle class

<img src="https://github.com/allwak/Introduction-to-python-programming-and-data-structures/blob/main/Chapter%2009%20-%20Objects%20and%20Classes/Ex%209.1%20-%20The%20Rectangle%20class/Task.jpg" /> 

# Solution
```python

class Rectangle:
    def __init__(self, width = 1, height = 2):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)
```