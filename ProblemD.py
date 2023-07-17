"""n = int(input())
cont = [int(x) for x in input().split(" ")]

count = 0
for index,x in enumerate(cont):
    if index == x:
        count += 1
print(count)
"""
from itertools import product

n = int(input())
nums = [int(x) for x in input().split(" ")]
pairs = []
for i in range(1,n + 1):
    pairs.append((nums[i-1],i))

count = 0
for i in pairs:
    for j in pairs:
        if i[0] == j[1] and i[1] == j[0]:
            count += 1
            pairs.remove(i)
            pairs.remove(j)
print(count)
