def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    x = str(x)
    length = len(x)
    half = length / 2

    if (length <= 1):
        return True

    for i in range(half):
        if (x[i] != x[length - 1 - i]):
            return False

    return True