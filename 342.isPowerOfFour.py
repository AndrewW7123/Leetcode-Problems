def isPowerOfFour(n):
    """
    :type n: int
    :rtype: bool
    """
    if (n <= 0):
        return False
    if (n == 4 or n == 1):
        return True
    
    power = 4
    while (power < n):
        power = power * 4

        if (power == n):
            return True
    
    power = 4
    while (power > n):
        power = power / 4

        if (power == n):
            return True

    return False