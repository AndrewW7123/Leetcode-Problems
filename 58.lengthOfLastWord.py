def lengthOfLastWord(s: str) -> int:
    """
    :type s: str
    :rtype: int
    """
    lastLength = 0
    curLength = 0

    for char in s:
        if (char == " "):
            curLength = 0
        else:
            curLength += 1
            lastLength = curLength

    return lastLength