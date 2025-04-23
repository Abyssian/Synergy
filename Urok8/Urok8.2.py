N = int(input())
arr = list(map(int, input().split()))
result = [arr[-1]] + [arr[i] for i in range(N - 1)]

print(*result)