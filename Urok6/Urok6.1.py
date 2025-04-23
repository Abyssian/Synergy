N = int(input("Введите количество чисел: "))
count = 0

for i in range(N):
    num = int(input())
    if num == 0:
        count += 1

print(count)