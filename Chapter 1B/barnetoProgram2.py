nums = [27, 5, 18, 66, 12, 5, 9]
nums.sort()

print("Median:", nums[int(len(nums) / 2)])
sum = 0
for i in range(len(nums)):
    sum += nums[i]

print("Mean:", sum / len(nums))
