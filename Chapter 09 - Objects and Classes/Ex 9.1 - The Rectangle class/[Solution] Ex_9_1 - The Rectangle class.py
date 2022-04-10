# Sum elements column by column

# Enter a 3-by-4 matrix row 0: 1.5 2 3 4
# Enter a 3-by-4 matrix row 1: 5.4 6 7 8
# Enter a 3-by-4 matrix row 2: 9 10 11 12
# Sum of the elements at column 0 is 15.9
# Sum of the elements at column 1 is 18.0
# Sum of the elements at column 2 is 21.0
# Sum of the elements at column 3 is 24.0

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