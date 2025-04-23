X = int(input("Введите число: "))
i = 1
count = 0

while i * i <= X:
    if X % i == 0:
        if i == X // i:
            count += 1
        else:
            count += 2
    i += 1

print(count)
#итого у 2 миллиарда 110 натуральных делителей