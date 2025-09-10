def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    elemNum = 0

    for elem in nums:
        elemNum = nums.count(elem)
        while (elemNum > 1):
            for elem2 in nums[nums.index(elem) + 1::]:
                if (elem2 == elem):
                    nums.pop(nums.index(elem2))
                    elemNum -= 1
        elemNum = 0

    return len(nums)