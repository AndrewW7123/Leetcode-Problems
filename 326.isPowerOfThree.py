def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    if (n <= 0):
        return False
    if (n == 1 or n == 3):
        return True
    
    count = 3
    while (count < n):
        count = count * 3
        if (count == n):
            return True
    
    count = 3
    while (count > n):
        count = count / 3
        if (count == n):
            return True
    
    return False