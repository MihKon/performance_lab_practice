import sys


input_file_path = sys.argv[1]
nums = []
result = 0
temp_results_arr = {}

with open(input_file_path, "r", encoding="UTF-8") as input_file:
    for line in input_file.readlines():
        nums.append(int(line))

for i in range(len(nums)):
    for j in range(i, len(nums)):
        diff = abs(nums[j] - nums[i])
        if nums[i] not in temp_results_arr.keys():
            temp_results_arr[nums[i]] = 0
        temp_results_arr[nums[i]] += diff
        if nums[j] not in temp_results_arr.keys():
            temp_results_arr[nums[j]] = 0
        temp_results_arr[nums[j]] += diff

result = min(temp_results_arr.values())
print(result)
