def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


def combination(n, r):
       return factorial(n) // (factorial(r) * factorial(n - r))


def pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            coef = combination(i, j)
            row.append(coef)
        triangle.append(row)

    return triangle

n = int(input("Enter the number of rows for Pascal's triangle: "))
T = pascals_triangle(n)
print("Pascal's Triangle:")
for row in T:
    for i in row:
        print(i, end=" ")
    print()