m1 = int(input('enter the no. of rows in matrix1'))
n1 = int(input('enter the no. of columns in matrix1'))

m2 = int(input('enter the no. of rows in matrix2'))
n2 = int(input('enter the no. of columns in matrix2'))

print('the order of matrix1 is:')
print(m1, "x", n1)

print('the order of matrix2 is:')
print(m2, "x", n2)

non_zero_values = {}

print('enter values in matrix1:')
for i in range(m1) :
    for j in range(n1) :
        value = int(input(f"enter value at {i+1}, enter value at {j+1}: "))
        if value!= 0 :
            non_zero_values[(i,j)] = value

print('enter values in matrix2:')
for i in range(m2) :
    for j in range(n2) :
        value = int(input(f"enter value at {i+1}, enter value at {j+1}: "))
        if value!= 0 :
            non_zero_values[(i,j + n1)] = value

print("Non-zero values in the combined matrix:")
for position, value in non_zero_values.items():
    row, col = position
    print(f"Value {value} at row {row + 1}, column {col + 1}")


# Input the order (number of rows and columns) of the matrices
rows = int(input("Enter the number of rows for the matrices: "))
cols = int(input("Enter the number of columns for the matrices: "))

# Initialize dictionaries for the first and second matrices
matrix1 = {}
matrix2 = {}

# Input the values of the first matrix
print("Enter the values of the first matrix:")
for i in range(rows):
    for j in range(cols):
        value = int(input(f"Enter the value at row {i + 1}, column {j + 1} for matrix 1: "))
        if value != 0:
            matrix1[(i, j)] = value

# Input the values of the second matrix
print("Enter the values of the second matrix:")
for i in range(rows):
    for j in range(cols):
        value = int(input(f"Enter the value at row {i + 1}, column {j + 1} for matrix 2: "))
        if value != 0:
            matrix2[(i, j)] = value

# Initialize a dictionary to store the result matrix
result_matrix = {}

# Add corresponding values from both matrices and store them in the result dictionary
for i in range(rows):
    for j in range(cols):
        value1 = matrix1.get((i, j), 0)  # Get value from matrix 1 (default to 0 if not present)
        value2 = matrix2.get((i, j), 0)  # Get value from matrix 2 (default to 0 if not present)
        result_matrix[(i, j)] = value1 + value2  # Store the sum in the result matrix

# Display the result matrix in two-dimensional form
print("Result Matrix:")
for i in range(rows):
    row_values = []
    for j in range(cols):
        row_values.append(result_matrix.get((i, j), 0))
    print(row_values)
