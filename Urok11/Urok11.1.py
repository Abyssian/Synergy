def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("Введите натуральное число: "))

fact_of_num = factorial(num)

fact_list = []

for i in range(fact_of_num, 0, -1):
    temp = 1
    j = 1
    while temp < i:
        j += 1
        temp *= j
    if temp == i:
        fact_list.append(i)

print(fact_list)