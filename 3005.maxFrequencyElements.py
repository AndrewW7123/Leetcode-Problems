def maxFrequencyElements(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    freq = {}
    maxFreq = 0
    numMaxFreq = 0

    for i in range(len(nums)):
        if nums[i] in freq:
            freq[nums[i]] += 1
        else:
            freq[nums[i]] = 1
    for j in freq:
        if freq[j] > maxFreq:
            maxFreq = freq[j]
            numMaxFreq = freq[j]
        elif freq[j] == maxFreq:
            numMaxFreq += freq[j]

    return numMaxFreq