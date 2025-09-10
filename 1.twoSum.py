def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    length = len(nums)
    i = 0

    while (i < length - 1):
        for j in range(i + 1, length):
            result = nums[i] + nums[j]
            if (result == target):
                return [i,j]
        i += 1

    return []