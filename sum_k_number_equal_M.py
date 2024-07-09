def find_combitions(nums, target):
    result = []
    find_combitions_recursive(nums, target, 0, [], result)
    return result
def find_combitions_recursive(nums, target, start, path, result):
    if target < 0:
        return 
    if target == 0:
        result.append(list(path))
    for i in range (start, len(nums)):
        path.append(nums[i])
        find_combitions_recursive(nums, target - nums[i], i+1, path, result)
        path.pop()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 4, 3, 1, 9, 6]
target = 7
result = find_combitions(nums, target)
print(result)