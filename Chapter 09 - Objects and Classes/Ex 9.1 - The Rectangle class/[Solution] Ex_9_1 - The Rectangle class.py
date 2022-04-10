# (The Rectangle class) Following the example of the Circle class in Section 9.2, 
# design a class named Rectangle to represent a rectangle. The class contains:
# Two data fields named width and height.
# A constructor that creates a rectangle with the specified width and height. 
# The default values are 1 and 2 for the width and height, respectively.

# A method named getArea() that returns the area of this rectangle.
# A method named getPerimeter() that returns the perimeter.

# Draw the UML diagram for the class, and then implement the class. 
# Write a test program that creates two Rectangle objects—one with width 4 and height 40 and the other with width 
# 3.5 and height 35.7. Display the width, height, area, and perimeter of each rectangle in this order.

# The width of the rectangle is 4
# The height of the rectangle is 40
# The area of the rectangle is 160
# The perimeter of the rectangle is 88
# The width of the rectangle is 3.5
# The height of the rectangle is 35.7
# The area of the rectangle is 124.95000000000002
# The perimeter of the rectangle is 78.4
class Rectangle:
    def __init__(self, width = 1, height = 2):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)

rect1 = Rectangle(4, 40)
rect2 = Rectangle(3.5, 35.7)

print("The width of the rectangle is", rect1.width)
print("The height of the rectangle is", rect1.height)
print("The area of the rectangle is", rect1.getArea())
print("The perimeter of the rectangle is", rect1.getPerimeter())
print("The width of the rectangle is", rect2.width)
print("The height of the rectangle is", rect2.height)
print("The area of the rectangle is", rect2.getArea())
print("The perimeter of the rectangle is", rect2.getPerimeter())
