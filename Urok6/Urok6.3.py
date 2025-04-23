A = int(input("Введите A: "))
B = int(input("Введите B: "))

for i in range(A, B + 1):
    if i % 2 == 0:
        print(i, end=' ')