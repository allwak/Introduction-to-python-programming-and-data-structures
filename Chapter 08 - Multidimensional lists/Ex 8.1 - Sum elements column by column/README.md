# Exercise 8.1 - Sum elements column by column

<img src="https://github.com/allwak/Introduction-to-python-programming-and-data-structures/blob/main/Chapter%2008%20-%20Multidimensional%20lists/Ex%208.1%20-%20Sum%20elements%20column%20by%20column/Task.jpg" /> 

# Solution
```python
def fill_matrix():
    matrix = []
    for i in range(3):
        row = [float(x) for x in input("Enter a 3-by-4 matrix row " + str(i) + ": ").split()]
        matrix.append(row) 
    return matrix

def sumColumn(matrix, columnIndex):
    sum = 0
    for row in matrix:
        sum += row[columnIndex]
    return sum

def main():
    matrix = fill_matrix()
    for i in range(4):
        print("Sum of the elements at column " + str(i) + " is " + str(sumColumn(matrix, i)))

main()
```