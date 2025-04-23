import random

rows = 10
cols = 10

matrix1 = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(-50, 200))
    matrix1.append(row)

matrix2 = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(-50, 200))
    matrix2.append(row)

result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

print("Матрица 1:")
for row in matrix1:
    print(row)

print("\nМатрица 2:")
for row in matrix2:
    print(row)

print("\nСумма матриц:")
for row in result:
    print(row)
