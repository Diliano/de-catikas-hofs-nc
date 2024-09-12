def some(nums, func):
    for num in nums:
        if func(num):
            return True
    return False