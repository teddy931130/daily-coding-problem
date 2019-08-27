import numpy

nums = list(map(int, input().split()))
temp_nums = []
new_nums = []


for index in range(len(nums)):
    temp_nums = nums[:index] + nums[index + 1:]
    temp = int(numpy.prod(temp_nums))
    new_nums.append(temp)
    temp_nums = []

print(new_nums)
