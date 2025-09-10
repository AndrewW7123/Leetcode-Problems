def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    ind = 0

    for i in nums:
        if (target == i):
            return ind
        if (target < i):
            return ind
        ind += 1

    return ind