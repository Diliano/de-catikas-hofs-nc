def every(nums, func):
    for num in nums:
        if not func(num):
            return False
    return True