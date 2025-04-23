n = int(input())
numbers = input().split()
unique_numbers = set()
for num in numbers:
    unique_numbers.add(int(num))

print(len(unique_numbers))