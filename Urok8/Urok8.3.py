m = int(input()) 
n = int(input())  
weights = [int(input()) for _ in range(n)]  

weights.sort()

i, j = 0, n - 1
boats = 0

while i <= j:
    if weights[i] + weights[j] <= m:
        i += 1
    j -= 1
    boats += 1

print(boats)

m = int(input())
n = int(input())

weights = [int(input()) for _ in range(n)]

boats = 0
i = 0
j = n - 1

while i <= j:
    if weights[i] + weights[j] <= m:
        i += 1
    j -= 1
    boats += 1

print(boats)