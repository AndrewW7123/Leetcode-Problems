def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    prefix = ""

    if (len(strs) < 1):
        return ""
    if (len(strs) == 1):
        return strs[0]

    minlength = len(strs[0])

    for word in strs:
        if word == "":
            return ""
        if (len(word) < minlength):
            minlength = len(word)

    for i in range(minlength):
        for word in strs[1::]:
            if (strs[0][i] != word[i]):
                return prefix
        prefix += strs[0][i]
    
    return prefix