def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    if (n <= 0):
        return False
    if (n == 1 or n == 2):
        return True
    
    count = 2
    while (count < n):
        count = count * 2
        if (count == n):
            return True
    
    count = 2
    while (count > n):
        count = count / 2
        if (count == n):
            return True
    
    return False