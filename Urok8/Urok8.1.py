N = int(input())  
numbers = []  

for _ in range(N):
    numbers.append(int(input()))
numbers.reverse()

print(*numbers)