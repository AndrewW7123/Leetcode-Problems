def maxFreqSum(s):
    """
    :type s: str
    :rtype: int
    """
    maxVowels = 0
    maxOthers = 0
    vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    others = {}

    for i in s:
        if (i in vowels):
            vowels[i] += 1
            if (vowels[i] > maxVowels):
                maxVowels = vowels[i]
        elif (i in others):
            others[i] += 1
            if (others[i] > maxOthers):
                maxOthers = others[i]
        else:
            others[i] = 0
            others[i] += 1
            if (others[i] > maxOthers):
                maxOthers = others[i]
                
    return maxVowels + maxOthers