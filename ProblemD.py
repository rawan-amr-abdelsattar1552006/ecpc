n = int(input())
nums = [int(x) for x in input().split(" ")]

count = 0

for i in nums:
    if nums[i - 1] == nums.index(i) + 1:
        count += 1
        
print(count // 2)
