def find(nums, func):
    for num in nums:
        if func(num):
            return num
    return "No element satisfies the predicate function"