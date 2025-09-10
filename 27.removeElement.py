def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    notval = 0
    valCount = 0
    l = len(nums)

    if (l < 1):
        return 0
    if (l == 1):
        if (nums[0] == val):
            return notval
        return 1

    if (val in nums):
        for i in range(l):
            for j in range(1, l):
                if (nums[j-1] == val):
                    nums[j-1], nums[j] = nums[j], nums[j-1]
    else:
        return l

    for i in range(l):
        if (nums[i] != val):
            notval += 1
    return notval