n = int(input())
set1 = set()
for _ in range(n):
    set1.add(int(input()))

m = int(input())
set2 = set()
for _ in range(m):
    set2.add(int(input()))
common_elements = set1.intersection(set2)

print(len(common_elements))